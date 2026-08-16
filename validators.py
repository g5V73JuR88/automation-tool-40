import re

def validate_input(user_input):
    if not isinstance(user_input, str):
        raise ValueError('Input must be a string')
    if len(user_input) == 0:
        raise ValueError('Input cannot be empty')
    if not re.match('^[a-zA-Z0-9_]+$', user_input):
        raise ValueError('Input must only contain alphanumeric characters and underscores')
    return True

# Example usage within the main processing loop

def process_input(user_input):
    try:
        validate_input(user_input)
        # Proceed with processing
    except ValueError as e:
        print(f'Input validation error: {e}')