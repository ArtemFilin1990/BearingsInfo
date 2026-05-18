"""Configuration management module."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict

import yaml


class ConfigValidationError(ValueError):
    """Raised when configuration files are missing or invalid."""


class Config:
    """Configuration manager."""

    def __init__(self, config_dir: Path | None = None):
        """Initialize configuration.

        Args:
            config_dir: Path to configuration directory
        """
        if config_dir is None:
            config_dir = Path(__file__).parent.parent / "config"

        self.config_dir = Path(config_dir)
        self._app_config: Dict[str, Any] | None = None
        self._brand_aliases: Dict[str, str] | None = None
        self._parsing_rules: Dict[str, Any] | None = None

    def load_app_config(self) -> Dict[str, Any]:
        """Load application configuration.

        Returns:
            Application configuration dictionary
        """
        if self._app_config is None:
            config_file = self.config_dir / "app.yaml"
            data = self._read_yaml(config_file)
            self._validate_app_config(data, config_file)
            self._app_config = data
        return self._app_config

    def load_brand_aliases(self) -> Dict[str, str]:
        """Load brand aliases mapping.

        Returns:
            Brand aliases dictionary
        """
        if self._brand_aliases is None:
            aliases_file = self.config_dir / "brand_aliases.json"
            data = self._read_json(aliases_file)
            self._validate_brand_aliases(data, aliases_file)
            self._brand_aliases = data["aliases"]
        return self._brand_aliases

    def load_parsing_rules(self) -> Dict[str, Any]:
        """Load parsing rules configuration.

        Returns:
            Parsing rules dictionary
        """
        if self._parsing_rules is None:
            rules_file = self.config_dir / "parsing_rules.json"
            data = self._read_json(rules_file)
            self._validate_parsing_rules(data, rules_file)
            self._parsing_rules = data
        return self._parsing_rules

    def get(self, key: str, default: Any = None) -> Any:
        """Get configuration value by key path.

        Args:
            key: Key path (e.g., 'watcher.mode')
            default: Default value if key not found

        Returns:
            Configuration value
        """
        config = self.load_app_config()
        keys = key.split(".")

        value: Any = config
        for k in keys:
            if isinstance(value, dict) and k in value:
                value = value[k]
            else:
                return default

        return value

    @staticmethod
    def _read_yaml(path: Path) -> Dict[str, Any]:
        try:
            with path.open("r", encoding="utf-8") as f:
                data = yaml.safe_load(f)
        except FileNotFoundError as exc:
            raise ConfigValidationError(
                f"Missing configuration file: {path}"
            ) from exc
        except OSError as exc:
            raise ConfigValidationError(
                f"Unable to read configuration file: {path}. Reason: {exc}"
            ) from exc
        except yaml.YAMLError as exc:
            raise ConfigValidationError(
                f"Invalid YAML in configuration file: {path}. Reason: {exc}"
            ) from exc

        if data is None:
            raise ConfigValidationError(
                f"Configuration file is empty: {path}"
            )
        if not isinstance(data, dict):
            raise ConfigValidationError(
                f"Configuration file must contain a mapping at top level: {path}"
            )
        return data

    @staticmethod
    def _read_json(path: Path) -> Dict[str, Any]:
        try:
            with path.open("r", encoding="utf-8") as f:
                data = json.load(f)
        except FileNotFoundError as exc:
            raise ConfigValidationError(
                f"Missing configuration file: {path}"
            ) from exc
        except json.JSONDecodeError as exc:
            raise ConfigValidationError(
                f"Invalid JSON in configuration file: {path}. "
                f"Reason: {exc.msg} (line {exc.lineno}, column {exc.colno})"
            ) from exc
        except OSError as exc:
            raise ConfigValidationError(
                f"Unable to read configuration file: {path}. Reason: {exc}"
            ) from exc

        if not isinstance(data, dict):
            raise ConfigValidationError(
                f"Configuration file must contain a mapping at top level: {path}"
            )
        return data

    @classmethod
    def _validate_app_config(cls, config: Dict[str, Any], path: Path) -> None:
        paths = cls._require_dict(config, "paths", path)
        for key in ("inbox", "processed", "error", "out"):
            cls._require_str(paths, key, path, allow_empty=False)
        if "logs" in paths:
            cls._require_str(paths, "logs", path, allow_empty=False)

        limits = cls._require_dict(config, "limits", path)
        cls._require_number(
            limits,
            "max_file_size_mb",
            path,
            min_value=0.0,
            allow_zero=False,
        )
        cls._require_int(limits, "max_rows", path, min_value=1)

        normalization = cls._require_dict(config, "normalization", path)
        cls._require_str(normalization, "brand_format", path)
        brand_format = normalization.get("brand_format")
        if brand_format not in {"title", "upper"}:
            raise ConfigValidationError(
                f"Invalid value for normalization.brand_format in {path}: "
                f"{brand_format!r}. Expected 'title' or 'upper'."
            )
        if "dimension_replacements" in normalization:
            replacements = cls._require_dict(
                normalization, "dimension_replacements", path
            )
            for key, value in replacements.items():
                if not isinstance(key, str) or not isinstance(value, str):
                    raise ConfigValidationError(
                        f"normalization.dimension_replacements must map strings to "
                        f"strings in {path}."
                    )
        cls._require_str(normalization, "decimal_separator", path)

        if "watcher" in config:
            watcher = cls._require_dict(config, "watcher", path)
            cls._require_str(watcher, "mode", path)
            mode = watcher.get("mode")
            if mode not in {"poll", "watch"}:
                raise ConfigValidationError(
                    f"Invalid value for watcher.mode in {path}: {mode!r}. "
                    "Expected 'poll' or 'watch'."
                )
            if mode == "poll":
                cls._require_int(
                    watcher, "poll_interval", path, min_value=1
                )
            if "process_on_start" in watcher:
                cls._require_bool(watcher, "process_on_start", path)

        if "output" in config:
            output = cls._require_dict(config, "output", path)
            cls._require_str(output, "csv_encoding", path)
            cls._require_str(output, "csv_delimiter", path)
            cls._require_int(output, "json_indent", path, min_value=0)
            if "csv_bom" in output:
                cls._require_bool(output, "csv_bom", path)

        if "logging" in config:
            logging_cfg = cls._require_dict(config, "logging", path)
            cls._require_str(logging_cfg, "level", path)
            level = logging_cfg.get("level")
            if level not in {"DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"}:
                raise ConfigValidationError(
                    f"Invalid value for logging.level in {path}: {level!r}."
                )
            cls._require_str(logging_cfg, "format", path)
            log_format = logging_cfg.get("format")
            if log_format not in {"json", "text"}:
                raise ConfigValidationError(
                    f"Invalid value for logging.format in {path}: {log_format!r}."
                )
            cls._require_number(
                logging_cfg,
                "max_size_mb",
                path,
                min_value=0.0,
                allow_zero=False,
            )
            cls._require_int(logging_cfg, "backup_count", path, min_value=0)

        if "registry" in config:
            registry = cls._require_dict(config, "registry", path)
            cls._require_str(registry, "file", path, allow_empty=False)
            if "allow_reprocess_errors" in registry:
                cls._require_bool(
                    registry, "allow_reprocess_errors", path
                )

    @classmethod
    def _validate_brand_aliases(cls, data: Dict[str, Any], path: Path) -> None:
        aliases = cls._require_dict(data, "aliases", path)
        for key, value in aliases.items():
            if not isinstance(key, str) or not isinstance(value, str):
                raise ConfigValidationError(
                    f"aliases must map strings to strings in {path}."
                )
            if not key.strip() or not value.strip():
                raise ConfigValidationError(
                    f"aliases cannot contain empty strings in {path}."
                )

    @classmethod
    def _validate_parsing_rules(cls, data: Dict[str, Any], path: Path) -> None:
        column_mappings = cls._require_dict(data, "column_mappings", path)
        for column, aliases in column_mappings.items():
            if not isinstance(column, str):
                raise ConfigValidationError(
                    f"column_mappings keys must be strings in {path}."
                )
            cls._require_str_list_value(
                aliases, f"column_mappings.{column}", path
            )

        patterns = cls._require_list(data, "dimension_patterns", path)
        for index, pattern in enumerate(patterns):
            if not isinstance(pattern, dict):
                raise ConfigValidationError(
                    f"dimension_patterns[{index}] must be an object in {path}."
                )
            cls._require_str(pattern, "regex", path)
            groups = cls._require_list(pattern, "groups", path)
            if not groups:
                raise ConfigValidationError(
                    f"dimension_patterns[{index}].groups must not be empty in {path}."
                )
            for group in groups:
                if not isinstance(group, str):
                    raise ConfigValidationError(
                        f"dimension_patterns[{index}].groups must be strings in {path}."
                    )

        required_fields = cls._require_dict(data, "required_fields", path)
        any_of = cls._require_list(required_fields, "any_of", path)
        if not any_of:
            raise ConfigValidationError(
                f"required_fields.any_of must not be empty in {path}."
            )
        for field in any_of:
            if not isinstance(field, str):
                raise ConfigValidationError(
                    f"required_fields.any_of must contain strings in {path}."
                )

        text_normalization = cls._require_dict(data, "text_normalization", path)
        cls._require_bool(text_normalization, "trim", path)
        cls._require_bool(text_normalization, "collapse_spaces", path)
        cls._require_bool(text_normalization, "remove_control_chars", path)

    @staticmethod
    def _require_dict(data: Dict[str, Any], key: str, path: Path) -> Dict[str, Any]:
        if key not in data:
            raise ConfigValidationError(
                f"Missing required key '{key}' in {path}."
            )
        value = data[key]
        if not isinstance(value, dict):
            raise ConfigValidationError(
                f"Expected '{key}' to be an object in {path}."
            )
        return value

    @staticmethod
    def _require_list(data: Dict[str, Any], key: str, path: Path) -> list[Any]:
        if key not in data:
            raise ConfigValidationError(
                f"Missing required key '{key}' in {path}."
            )
        value = data[key]
        if not isinstance(value, list):
            raise ConfigValidationError(
                f"Expected '{key}' to be an array in {path}."
            )
        return value

    @staticmethod
    def _require_list_of_str(
        data: Dict[str, Any], key: str, path: Path
    ) -> list[str]:
        value = Config._require_list(data, key, path)
        return Config._require_str_list_value(value, key, path)

    @staticmethod
    def _require_str_list_value(
        value: Any, key: str, path: Path
    ) -> list[str]:
        if not isinstance(value, list):
            raise ConfigValidationError(
                f"Expected '{key}' to be an array in {path}."
            )
        if not value:
            raise ConfigValidationError(
                f"Expected '{key}' to contain at least one value in {path}."
            )
        for item in value:
            if not isinstance(item, str):
                raise ConfigValidationError(
                    f"Expected '{key}' to contain strings in {path}."
                )
        return value

    @staticmethod
    def _require_str(
        data: Dict[str, Any],
        key: str,
        path: Path,
        allow_empty: bool = False,
    ) -> str:
        if key not in data:
            raise ConfigValidationError(
                f"Missing required key '{key}' in {path}."
            )
        value = data[key]
        if not isinstance(value, str):
            raise ConfigValidationError(
                f"Expected '{key}' to be a string in {path}."
            )
        if not allow_empty and not value.strip():
            raise ConfigValidationError(
                f"Expected '{key}' to be a non-empty string in {path}."
            )
        return value

    @staticmethod
    def _require_bool(data: Dict[str, Any], key: str, path: Path) -> bool:
        if key not in data:
            raise ConfigValidationError(
                f"Missing required key '{key}' in {path}."
            )
        value = data[key]
        if not isinstance(value, bool):
            raise ConfigValidationError(
                f"Expected '{key}' to be a boolean in {path}."
            )
        return value

    @staticmethod
    def _require_int(
        data: Dict[str, Any],
        key: str,
        path: Path,
        min_value: int | None = None,
    ) -> int:
        if key not in data:
            raise ConfigValidationError(
                f"Missing required key '{key}' in {path}."
            )
        value = data[key]
        if not isinstance(value, int) or isinstance(value, bool):
            raise ConfigValidationError(
                f"Expected '{key}' to be an integer in {path}."
            )
        if min_value is not None and value < min_value:
            raise ConfigValidationError(
                f"Expected '{key}' to be >= {min_value} in {path}."
            )
        return value

    @staticmethod
    def _require_number(
        data: Dict[str, Any],
        key: str,
        path: Path,
        min_value: float | None = None,
        allow_zero: bool = True,
    ) -> float:
        if key not in data:
            raise ConfigValidationError(
                f"Missing required key '{key}' in {path}."
            )
        value = data[key]
        if not isinstance(value, (int, float)) or isinstance(value, bool):
            raise ConfigValidationError(
                f"Expected '{key}' to be a number in {path}."
            )
        numeric_value = float(value)
        if min_value is not None:
            if allow_zero and numeric_value < min_value:
                raise ConfigValidationError(
                    f"Expected '{key}' to be >= {min_value} in {path}."
                )
            if not allow_zero and numeric_value <= min_value:
                raise ConfigValidationError(
                    f"Expected '{key}' to be > {min_value} in {path}."
                )
        return numeric_value
