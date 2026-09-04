from typing import Any, Dict, Optional

def validate_input_schema(data: Any, required_keys: list) -> bool:
    if not isinstance(data, dict):
        return False
    return all(key in data for key in required_keys)

def sanitize_input(data: Dict[str, Any]) -> Dict[str, Any]:
    return {k: str(v).strip() for k, v in data.items() if v is not None}

def process_main_loop(items: list, required: list) -> list:
    results = []
    for item in items:
        if not validate_input_schema(item, required):
            continue
        try:
            clean_data = sanitize_input(item)
            results.append(clean_data)
        except (ValueError, TypeError):
            continue
    return results