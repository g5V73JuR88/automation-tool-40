import re

def validate_input(data):
    if not isinstance(data, str):
        raise ValueError('Input must be a string')
    if not data:
        raise ValueError('Input cannot be empty')
    if len(data) < 3:
        raise ValueError('Input must be at least 3 characters long')
    if not re.match('^[a-zA-Z0-9 _-]*$', data):
        raise ValueError('Input contains invalid characters')

    return True

