import json
import os
from pathlib import Path
from typing import Any, Dict, Optional

def read_json(file_path: str) -> Dict[str, Any]:
    path = Path(file_path)
    if not path.exists():
        return {}
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def write_json(file_path: str, data: Dict[str, Any]) -> None:
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

def ensure_directory(directory_path: str) -> None:
    Path(directory_path).mkdir(parents=True, exist_ok=True)

def get_env_variable(key: str, default: Optional[str] = None) -> str:
    return os.getenv(key, default or '')

def format_byte_size(size: int) -> str:
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size < 1024:
            return f"{size:.2f} {unit}"
        size /= 1024
    return f"{size:.2f} TB"

def flatten_dict(d: Dict, parent_key: str = '', sep: str = '_') -> Dict:
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)