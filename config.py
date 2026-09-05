import os
from typing import Dict, Any, Optional

class Config:
    """Centralized configuration management for automation-tool-40."""

    def __init__(self, env: str = "development") -> None:
        self.env: str = env
        self.settings: Dict[str, Any] = self._load_settings()

    def _load_settings(self) -> Dict[str, Any]:
        """Retrieve configuration settings based on environment."""
        return {
            "debug": os.getenv("DEBUG", "True") == "True",
            "timeout": int(os.getenv("TIMEOUT", "30")),
            "max_retries": int(os.getenv("MAX_RETRIES", "3")),
            "log_level": os.getenv("LOG_LEVEL", "INFO")
        }

    def get(self, key: str, default: Optional[Any] = None) -> Any:
        """Fetch a configuration value by key."""
        return self.settings.get(key, default)

    def update(self, key: str, value: Any) -> None:
        """Update a specific configuration setting."""
        self.settings[key] = value

def get_config() -> Config:
    """Factory function to instantiate configuration."""
    return Config(env=os.getenv("APP_ENV", "production"))