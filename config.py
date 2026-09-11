import json
import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "retries": 3,
    "timeout": 30,
    "log_level": "INFO",
    "enabled": True
}

def load_config(path: str) -> Dict[str, Any]:
    config = DEFAULT_CONFIG.copy()
    if os.path.exists(path):
        with open(path, "r") as f:
            try:
                user_data = json.load(f)
                config.update(user_data)
            except json.JSONDecodeError:
                pass
    return config

def validate_config(config: Dict[str, Any]) -> None:
    required_keys = {"retries", "timeout", "log_level", "enabled"}
    if not required_keys.issubset(config.keys()):
        raise ValueError(f"missing required keys: {required_keys - config.keys()}")

if __name__ == "__main__":
    cfg = load_config("config.json")
    validate_config(cfg)
    print(f"Config loaded: {cfg}")