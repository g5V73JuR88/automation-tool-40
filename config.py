import json
import os
from typing import Any, Dict

class ConfigLoader:
    def __init__(self, defaults: Dict[str, Any] = None):
        self.defaults = defaults or {}
        self._config: Dict[str, Any] = self.defaults.copy()

    def load_from_file(self, filepath: str) -> None:
        if os.path.exists(filepath):
            with open(filepath, 'r') as f:
                data = json.load(f)
                self._config.update(data)

    def get(self, key: str, default: Any = None) -> Any:
        return self._config.get(key, default)

    def __getitem__(self, key: str) -> Any:
        return self._config[key]

    def __repr__(self) -> str:
        return f"ConfigLoader(data={self._config})"