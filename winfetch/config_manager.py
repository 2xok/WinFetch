"""
Configuration file manager.
"""
import os
from pathlib import Path
from typing import Optional, Dict, Any

try:
    import yaml
    YAML_AVAILABLE = True
except ImportError:
    YAML_AVAILABLE = False


class ConfigManager:
    """Manage configuration files."""
    
    def __init__(self, config_path: Optional[str] = None):
        self.config_path = self._get_config_path(config_path)
        self._config = None

    def _get_config_path(self, custom_path: Optional[str]) -> Path:
        """Get the path to the configuration file."""
        if custom_path:
            return Path(custom_path)
        
        # Default config locations
        if os.name == 'nt':  # Windows
            config_dir = Path.home() / "AppData" / "Local" / "winfetch"
        else:
            config_dir = Path.home() / ".config" / "winfetch"
        
        config_dir.mkdir(parents=True, exist_ok=True)
        return config_dir / "config.yaml"

    def load(self) -> Dict[str, Any]:
        """Load configuration from file."""
        if self._config is not None:
            return self._config

        defaults = {
            "colors": True,
            "ascii_art": "windows",
            "show_info": {
                "user": True,
                "hostname": True,
                "os": True,
                "kernel": True,
                "uptime": True,
                "packages": False,  # Can be slow on Windows
                "shell": True,
                "terminal": True,
                "cpu": True,
                "memory": True,
                "gpu": True,
                "disk": True,
                "network": True,
            },
            "colors": {
                "header": "cyan",
                "info": "white",
                "accent": "bright_blue"
            }
        }

        if not self.config_path.exists():
            self._config = defaults
            self._create_default_config()
            return self._config

        try:
            if YAML_AVAILABLE:
                with open(self.config_path, 'r', encoding='utf-8') as f:
                    user_config = yaml.safe_load(f) or {}
            else:
                # Simple fallback parsing for basic key=value format
                user_config = self._parse_simple_config()
            
            # Merge with defaults
            self._config = self._merge_configs(defaults, user_config)
            return self._config

        except Exception as e:
            print(f"Warning: Could not load config file: {e}")
            self._config = defaults
            return self._config

    def _create_default_config(self):
        """Create a default configuration file."""
        if not YAML_AVAILABLE:
            return
        
        try:
            with open(self.config_path, 'w', encoding='utf-8') as f:
                yaml.dump(self._config, f, default_flow_style=False, indent=2)
        except Exception as e:
            print(f"Warning: Could not create default config file: {e}")

    def _parse_simple_config(self) -> Dict[str, Any]:
        """Simple fallback config parser when YAML is not available."""
        config = {}
        try:
            with open(self.config_path, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith('#') and '=' in line:
                        key, value = line.split('=', 1)
                        key = key.strip()
                        value = value.strip()
                        
                        # Simple type conversion
                        if value.lower() in ('true', 'yes', '1'):
                            value = True
                        elif value.lower() in ('false', 'no', '0'):
                            value = False
                        elif value.isdigit():
                            value = int(value)
                        
                        config[key] = value
        except Exception:
            pass
        
        return config

    def _merge_configs(self, defaults: Dict[str, Any], user: Dict[str, Any]) -> Dict[str, Any]:
        """Recursively merge user config with defaults."""
        result = defaults.copy()
        
        for key, value in user.items():
            if key in result and isinstance(result[key], dict) and isinstance(value, dict):
                result[key] = self._merge_configs(result[key], value)
            else:
                result[key] = value
        
        return result

    def get(self, key: str, default: Any = None) -> Any:
        """Get a configuration value."""
        config = self.load()
        return config.get(key, default)

    def save(self, config: Dict[str, Any]):
        """Save configuration to file."""
        if not YAML_AVAILABLE:
            print("Warning: Cannot save config - YAML library not available")
            return
        
        try:
            self.config_path.parent.mkdir(parents=True, exist_ok=True)
            with open(self.config_path, 'w', encoding='utf-8') as f:
                yaml.dump(config, f, default_flow_style=False, indent=2)
            self._config = config
        except Exception as e:
            print(f"Error saving config: {e}")
