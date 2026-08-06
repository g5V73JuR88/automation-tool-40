import json
import re

def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def validate_json(data):
    try:
        json_object = json.loads(data)
    except ValueError as e:
        return False, str(e)
    return True, json_object

def is_positive_integer(value):
    if isinstance(value, int) and value > 0:
        return True
    return False

def validate_inputs(email, json_data, integer_value):
    email_valid = is_valid_email(email)
    json_valid, json_object = validate_json(json_data)
    integer_valid = is_positive_integer(integer_value)
    return {
        'email_valid': email_valid,
        'json_valid': json_valid,
        'integer_valid': integer_valid,
        'json_object': json_object if json_valid else None
    }