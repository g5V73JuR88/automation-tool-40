import logging

class CustomError(Exception):
    pass

def safe_divide(num1, num2):
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        raise CustomError('Inputs must be numbers')
    if num2 == 0:
        raise CustomError('Division by zero is not allowed')
    return num1 / num2


def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        logging.error('File not found: %s', file_path)
        raise CustomError('File not found')
    except IOError:
        logging.error('Error reading file: %s', file_path)
        raise CustomError('Error reading file')


def parse_json(json_string):
    import json
    try:
        return json.loads(json_string)
    except json.JSONDecodeError:
        logging.error('Invalid JSON: %s', json_string)
        raise CustomError('Invalid JSON format')
