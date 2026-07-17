def validate_input(data):
    if not isinstance(data, dict):
        raise ValueError('Input must be a dictionary')
    if 'value' not in data:
        raise KeyError('Missing key: value')
    if not isinstance(data['value'], (int, float)):
        raise TypeError('Value must be an integer or float')
    return True

def validate_range(value, min_value=0, max_value=100):
    if not (min_value <= value <= max_value):
        raise ValueError(f'Value {value} out of range ({min_value}-{max_value})')
    return True

# Example of using validation in a main processing loop:
try:
    input_data = {'value': 50}
    validate_input(input_data)
    validate_range(input_data['value'])
except (ValueError, KeyError, TypeError) as e:
    print(f'Validation Error: {e}')