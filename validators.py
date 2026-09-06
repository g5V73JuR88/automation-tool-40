from typing import Any, Dict, List, Tuple


class ValidationError(Exception):
    pass


def validate_task_config(config: Dict[str, Any]) -> Tuple[bool, List[str]]:
    errors = []
    if not isinstance(config, dict):
        return False, ["Task configuration must be a dictionary"]

    required_fields = ["id", "action", "params"]
    for field in required_fields:
        if field not in config:
            errors.append(f"Missing required field: '{field}'")

    if "id" in config and not isinstance(config["id"], (str, int)):
        errors.append("Field 'id' must be a string or integer")

    if "action" in config:
        if not isinstance(config["action"], str) or not config["action"].strip():
            errors.append("Field 'action' must be a non-empty string")

    if "params" in config and not isinstance(config["params"], dict):
        errors.append("Field 'params' must be a dictionary")

    if "timeout" in config:
        timeout = config["timeout"]
        if not isinstance(timeout, (int, float)) or timeout <= 0:
            errors.append("Field 'timeout' must be a positive number")

    return len(errors) == 0, errors


def validate_batch_inputs(tasks: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    valid_tasks = []
    for task in tasks:
        is_valid, errors = validate_task_config(task)
        if not is_valid:
            task_id = task.get("id", "unknown") if isinstance(task, dict) else "unknown"
            raise ValidationError(f"Task {task_id} validation failed: {'; '.join(errors)}")
        valid_tasks.append(task)
    return valid_tasks
