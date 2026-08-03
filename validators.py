import re

def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def is_valid_phone_number(phone):
    pattern = r'^(\+\d{1,3})?\d{10}$'
    return re.match(pattern, phone) is not None

def is_positive_integer(value):
    return isinstance(value, int) and value > 0

def is_not_empty_string(value):
    return isinstance(value, str) and len(value) > 0

def is_valid_url(url):
    pattern = r'^(https?://)?(www\.)?([a-zA-Z0-9]+\.)+[a-zA-Z]{2,}/?$'
    return re.match(pattern, url) is not None
