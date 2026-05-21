"""Catalog management module."""

import json
import logging
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import pandas as pd

from .utils import atomic_write, normalize_brand, normalize_number, normalize_text

_log = logging.getLogger(__name__)


class CatalogManager:
    """Manage bearing catalog."""
    
    # Target schema columns
    TARGET_COLUMNS = ['Наименование', 'Артикул', 'Аналог', 'Бренд', 'D', 'd', 'H', 'm']
    
    def __init__(
        self,
        catalog_csv: Path,
        catalog_json: Path,
        brand_aliases: Dict[str, str],
        normalization_config: Dict[str, Any]
    ):
        """Initialize catalog manager.
        
        Args:
            catalog_csv: Path to catalog CSV file
            catalog_json: Path to catalog JSON file
            brand_aliases: Brand aliases mapping
            normalization_config: Normalization configuration
        """
        self.catalog_csv = catalog_csv
        self.catalog_json = catalog_json
        self.brand_aliases = brand_aliases
        self.normalization_config = normalization_config
        
        # Create output directory
        self.catalog_csv.parent.mkdir(parents=True, exist_ok=True)

        # Load existing catalog and build the dedup index from it once
        self.catalog = self._load_catalog()
        self._dedup_index: dict[tuple, list[tuple]] = self._build_dedup_index(self.catalog)
    
    def _load_catalog(self) -> pd.DataFrame:
        """Load existing catalog or create empty one.
        
        Returns:
            Catalog DataFrame
        """
        if self.catalog_csv.exists():
            try:
                df = pd.read_csv(self.catalog_csv, encoding='utf-8')
                # Ensure all target columns exist
                for col in self.TARGET_COLUMNS:
                    if col not in df.columns:
                        df[col] = None
                return df[self.TARGET_COLUMNS]
            except Exception:
                _log.warning("Failed to load catalog from %s — starting empty", self.catalog_csv, exc_info=True)
        
        # Create empty catalog with target schema
        return pd.DataFrame(columns=self.TARGET_COLUMNS)

    @staticmethod
    def _build_dedup_index(df: pd.DataFrame) -> dict[tuple, list[tuple]]:
        """Build a dedup index from a catalog DataFrame.

        Structure: {(article, brand | None): [(D, d, H), ...]}
        """
        index: dict[tuple, list[tuple]] = {}
        for row in df.itertuples(index=False):
            art = row.Артикул
            if pd.isna(art) or art == '':
                continue
            brd = row.Бренд if pd.notna(row.Бренд) and row.Бренд != '' else None
            key = (art, brd)
            index.setdefault(key, []).append((row.D, row.d, row.H))
        return index
    
    def normalize_data(self, df: pd.DataFrame) -> pd.DataFrame:
        """Normalize data to target schema.
        
        Args:
            df: Input DataFrame
            
        Returns:
            Normalized DataFrame
        """
        # Create result with proper index
        result = pd.DataFrame(index=df.index)
        
        # Map and normalize each column
        for col in self.TARGET_COLUMNS:
            if col in df.columns:
                # Handle case where column name appears multiple times
                col_data = df[col]
                if isinstance(col_data, pd.DataFrame):
                    # Take first column if multiple
                    result[col] = col_data.iloc[:, 0]
                else:
                    result[col] = col_data
            else:
                result[col] = None
        
        # Normalize text fields
        text_fields = ['Наименование', 'Артикул', 'Аналог', 'Бренд']
        for field in text_fields:
            if field in result.columns:
                result[field] = result[field].apply(
                    lambda x: normalize_text(x, self.normalization_config) if pd.notna(x) else None
                )
        
        # Normalize brand
        brand_format = self.normalization_config.get('brand_format', 'upper')
        if 'Бренд' in result.columns:
            result['Бренд'] = result['Бренд'].apply(
                lambda x: normalize_brand(x, self.brand_aliases, brand_format) if pd.notna(x) else ""
            )
        
        # Normalize numeric fields
        numeric_fields = ['D', 'd', 'H', 'm']
        for field in numeric_fields:
            if field in result.columns:
                result[field] = result[field].apply(normalize_number)
        
        return result
    
    def add_records(
        self,
        new_data: pd.DataFrame
    ) -> Tuple[int, int, int, List[Dict[str, Any]]]:
        """Add new records to catalog with deduplication.
        
        Args:
            new_data: New data to add
            
        Returns:
            Tuple of (n_added, n_skipped, n_conflicts, conflicts_list)
        """
        if len(new_data) == 0:
            return 0, 0, 0, []

        # Normalize new data
        normalized = self.normalize_data(new_data)

        n_added = 0
        n_skipped = 0
        n_conflicts = 0
        conflicts = []
        # Collect dicts for accepted rows; pd.DataFrame(list[dict]) is clean and fast
        new_rows: List[Dict[str, Any]] = []

        for row in normalized.itertuples(index=False):
            art = row.Артикул
            if pd.isna(art) or art == '':
                n_skipped += 1
                continue

            brd = row.Бренд if pd.notna(row.Бренд) and row.Бренд != '' else None
            key = (art, brd)
            dims = (row.D, row.d, row.H)

            existing_dims_list = self._dedup_index.get(key, [])

            if dims in existing_dims_list:
                n_skipped += 1
                continue

            if existing_dims_list:
                # Dimensions differ for same (article, brand) — conflict
                conflict_info: Dict[str, Any] = {
                    'артикул': art,
                    'бренд': brd or '',
                    'new_dimensions': {'D': row.D, 'd': row.d, 'H': row.H},
                    'existing_dimensions': [
                        {'D': d[0], 'd': d[1], 'H': d[2]} for d in existing_dims_list
                    ],
                }
                n_conflicts += 1
                conflicts.append(conflict_info)

            # Accept row; update the persistent index so later rows in this file see it
            self._dedup_index.setdefault(key, []).append(dims)
            new_rows.append(row._asdict())
            n_added += 1

        if new_rows:
            self.catalog = pd.concat(
                [self.catalog, pd.DataFrame(new_rows)], ignore_index=True
            )

        return n_added, n_skipped, n_conflicts, conflicts
    
    def save(self) -> None:
        """Save catalog to CSV and JSON files atomically."""
        # Sort catalog for consistency
        if len(self.catalog) > 0:
            self.catalog = self.catalog.sort_values(
                by=['Бренд', 'Артикул'],
                na_position='last'
            ).reset_index(drop=True)
        
        # Save CSV
        csv_content = self.catalog.to_csv(index=False, encoding='utf-8')
        atomic_write(csv_content, self.catalog_csv)
        
        # Save JSON
        records = self.catalog.to_dict('records')
        # Convert NaN to None for JSON
        for record in records:
            for key, value in record.items():
                if pd.isna(value):
                    record[key] = None
        
        json_content = json.dumps(records, ensure_ascii=False, indent=2)
        atomic_write(json_content, self.catalog_json)
    
    def rebuild_from_processed(self, processed_dir: Path, parser) -> Tuple[int, int]:
        """Rebuild catalog from processed files.
        
        Args:
            processed_dir: Directory with processed files
            parser: DataParser instance
            
        Returns:
            Tuple of (n_files_processed, n_records_added)
        """
        # Clear current catalog and its dedup index
        self.catalog = pd.DataFrame(columns=self.TARGET_COLUMNS)
        self._dedup_index = {}
        
        n_files = 0
        n_records = 0
        
        # Process all files in processed directory
        for file_path in sorted(processed_dir.glob('*')):
            if file_path.is_file() and not file_path.name.startswith('.'):
                try:
                    # Determine file type from original extension
                    ext = file_path.suffix.lower()
                    if ext == '.csv':
                        file_type = 'csv'
                    elif ext in ['.xlsx', '.xls']:
                        file_type = 'xlsx'
                    elif ext == '.json':
                        file_type = 'json'
                    elif ext in ['.txt', '.md']:
                        file_type = 'txt'
                    else:
                        continue
                    
                    # Parse file
                    df = parser.parse_file(file_path, file_type)
                    df = parser.normalize_columns(df)
                    df = parser.validate_required_fields(df)
                    
                    # Add to catalog
                    n_added, _, _, _ = self.add_records(df)
                    
                    n_files += 1
                    n_records += n_added
                    
                except Exception:
                    # Skip files that can't be processed
                    continue
        
        # Save rebuilt catalog
        self.save()
        
        return n_files, n_records
