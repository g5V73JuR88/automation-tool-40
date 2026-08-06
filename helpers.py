def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()


def write_file(file_path, data):
    with open(file_path, 'w') as file:
        file.write(data)


def parse_json(json_str):
    import json
    return json.loads(json_str)


def format_timestamp(timestamp):
    from datetime import datetime
    return datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')


def generate_random_string(length=10):
    import random
    import string
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


def is_valid_email(email):
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))
