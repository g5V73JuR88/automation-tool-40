def validate_task(task):
    if not task:
        raise ValueError("Task cannot be empty")
    if not isinstance(task, dict):
        raise TypeError("Task must be a dictionary")
    if "action" not in task:
        raise KeyError("Task must have an action")
    return True

def execute_task(task):
    validate_task(task)
    action = task["action"]
    try:
        if action == "divide":
            numerator = task.get("numerator", 0)
            denominator = task.get("denominator", 1)
            if denominator == 0:
                raise ZeroDivisionError("Denominator cannot be zero")
            return numerator / denominator
        elif action == "list_sum":
            items = task.get("items", [])
            if not isinstance(items, list):
                raise TypeError("Items must be a list")
            if not items:
                raise ValueError("Items list cannot be empty")
            return sum(items)
        elif action == "concat":
            parts = task.get("parts", [])
            if not parts:
                raise ValueError("Parts cannot be empty")
            return "".join(str(p) for p in parts)
        else:
            raise ValueError("Unknown action: {}".format(action))
    except Exception as e:
        return {"error": str(e)}

def run_automation(tasks):
    if not isinstance(tasks, list):
        raise TypeError("Tasks must be a list")
    if not tasks:
        raise ValueError("No tasks provided")
    results = []
    for task in tasks:
        try:
            result = execute_task(task)
            if isinstance(result, dict) and "error" in result:
                results.append({"task": task.get("action", "unknown"), "status": "failed", "error": result["error"]})
            else:
                results.append({"task": task.get("action", "unknown"), "status": "success", "result": result})
        except Exception as e:
            results.append({"task": task.get("action", "unknown"), "status": "failed", "error": str(e)})
    return results

if __name__ == "__main__":
    sample_tasks = [
        {"action": "divide", "numerator": 10, "denominator": 2},
        {"action": "divide", "numerator": 10, "denominator": 0},
        {"action": "list_sum", "items": [1, 2, 3]},
        {"action": "list_sum", "items": []},
        {"action": "concat", "parts": ["hello", " ", "world"]},
        {"action": "concat", "parts": []},
        {"action": "unknown"},
        {},
        "not a dict"
    ]
    print(run_automation(sample_tasks))