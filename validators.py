import re

def is_valid_email(email):
    pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    return re.match(pattern, email) is not None

def is_non_empty_string(value):
    return isinstance(value, str) and bool(value.strip())

def is_in_range(value, min_value, max_value):
    return isinstance(value, (int, float)) and min_value <= value <= max_value

def is_valid_url(url):
    pattern = r'^(http|https)://[\w.-]+[\w.-]+'  
    return re.match(pattern, url) is not None

def is_numeric(value):
    return isinstance(value, (int, float))
