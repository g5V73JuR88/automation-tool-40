import re

def is_valid_input(user_input):
    if not isinstance(user_input, str):
        return False
    if len(user_input) == 0:
        return False
    if not re.match(r'^[a-zA-Z0-9_]*$', user_input):
        return False
    return True


def validate_and_process(user_input):
    if is_valid_input(user_input):
        # Process the valid input
        return f'Processed input: {user_input}'
    else:
        return 'Invalid input', 400