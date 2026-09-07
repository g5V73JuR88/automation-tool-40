import os
from pathlib import Path
from typing import Dict, Any

BASE_DIR = Path(__file__).resolve().parent

DEFAULT_CONFIG: Dict[str, Any] = {
    "log_level": "INFO",
    "max_retries": 3,
    "timeout": 30,
    "workspace": BASE_DIR / "workspace",
}

class Config:
    def __init__(self, overrides: Dict[str, Any] = None):
        self._settings = {**DEFAULT_CONFIG, **(overrides or {})}
        self._load_env_vars()

    def _load_env_vars(self) -> None:
        for key in self._settings.keys():
            env_val = os.getenv(f"APP_{key.upper()}")
            if env_val:
                self._settings[key] = env_val

    def get(self, key: str, default: Any = None) -> Any:
        return self._settings.get(key, default)

    @property
    def settings(self) -> Dict[str, Any]:
        return self._settings.copy()