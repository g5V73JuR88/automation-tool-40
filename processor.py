import json
import string
import re

class InputValidationError(Exception):
    pass

def is_valid_input(user_input):
    if not isinstance(user_input, str):
        raise InputValidationError("Input must be a string")
    if not user_input:
        raise InputValidationError("Input cannot be empty")
    if not re.match('^[a-zA-Z0-9_]*$', user_input):
        raise InputValidationError("Input contains invalid characters")

def main_processing_loop(inputs):
    results = []
    for user_input in inputs:
        try:
            is_valid_input(user_input)
            result = f"Processed: {user_input}"
            results.append(result)
        except InputValidationError as e:
            results.append(f"Error: {str(e)}")
    return json.dumps(results)

if __name__ == '__main__':
    sample_inputs = ["valid_input1", "invalid input!", ""]
    print(main_processing_loop(sample_inputs))
