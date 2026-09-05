import json
import os
from pathlib import Path
from typing import Any, Dict, Optional

def load_json(path: str) -> Dict[str, Any]:
    file_path = Path(path)
    if not file_path.exists():
        return {}
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json(path: str, data: Dict[str, Any]) -> None:
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

def ensure_dir(path: str) -> None:
    Path(path).mkdir(parents=True, exist_ok=True)

def get_env(key: str, default: Optional[str] = None) -> str:
    return os.getenv(key, default) or ''

def format_path(path: str) -> str:
    return str(Path(path).expanduser().resolve())