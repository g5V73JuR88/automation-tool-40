def safe_divide(numerator, denominator):
    if denominator == 0:
        raise ValueError("Denominator cannot be zero.")
    return numerator / denominator


def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except IOError:
        raise IOError(f"Error reading file: {file_path}")


def parse_json(json_string):
    import json
    try:
        return json.loads(json_string)
    except json.JSONDecodeError:
        raise ValueError("Invalid JSON string.")


def validate_age(age):
    if not isinstance(age, int) or age < 0:
        raise ValueError("Age must be a non-negative integer.")
    return True


if __name__ == '__main__':
    pass