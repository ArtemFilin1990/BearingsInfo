"""Registry management for tracking processed files."""

import json
from pathlib import Path
from typing import Any, Dict, Optional

from .utils import atomic_write


class Registry:
    """Manage registry of processed files."""
    
    def __init__(self, registry_file: Path):
        """Initialize registry.
        
        Args:
            registry_file: Path to registry JSON file
        """
        self.registry_file = registry_file
        self.registry_file.parent.mkdir(parents=True, exist_ok=True)
        self._data: Dict[str, Dict[str, Any]] = {}
        self._load()
    
    def _load(self) -> None:
        """Load registry from file."""
        if self.registry_file.exists():
            try:
                with open(self.registry_file, 'r', encoding='utf-8') as f:
                    self._data = json.load(f)
            except (json.JSONDecodeError, IOError):
                self._data = {}
        else:
            self._data = {}
    
    def _save(self) -> None:
        """Save registry to file atomically."""
        atomic_write(json.dumps(self._data, indent=2, ensure_ascii=False), self.registry_file)
    
    def is_processed(self, file_hash: str) -> bool:
        """Check if file has been processed.
        
        Args:
            file_hash: SHA256 hash of file
            
        Returns:
            True if file has been processed
        """
        return file_hash in self._data
    
    def add_entry(
        self,
        file_hash: str,
        original_name: str,
        processed_name: str,
        n_records: int,
        status: str = 'success',
        error_code: str | None = None,
        error_message: str | None = None,
    ) -> None:
        """Add entry to registry.
        
        Args:
            file_hash: SHA256 hash of file
            original_name: Original filename
            processed_name: Processed filename
            n_records: Number of records processed
            status: Processing status
            error_code: Optional error code
            error_message: Optional error message
        """
        entry = {
            'original_name': original_name,
            'processed_name': processed_name,
            'n_records': n_records,
            'status': status,
        }
        if error_code:
            entry['error_code'] = error_code
        if error_message:
            entry['error_message'] = error_message
        self._data[file_hash] = entry
        self._save()
    
    def get_entry(self, file_hash: str) -> Optional[Dict[str, Any]]:
        """Get registry entry for a file.
        
        Args:
            file_hash: SHA256 hash of file
            
        Returns:
            Registry entry or None
        """
        return self._data.get(file_hash)
    
    def get_all_entries(self) -> Dict[str, Dict[str, Any]]:
        """Get all registry entries.
        
        Returns:
            All registry entries
        """
        return self._data.copy()
