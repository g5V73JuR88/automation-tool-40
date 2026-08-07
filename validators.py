import re

def validate_email(email: str) -> bool:
    pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}''
    return re.match(pattern, email) is not None


def validate_phone(phone: str) -> bool:
    pattern = r'\+?1?\d{9,15}'
    return re.match(pattern, phone) is not None


def validate_url(url: str) -> bool:
    pattern = r'^(http|https)://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(/\S*)?''
    return re.match(pattern, url) is not None


def validate_password(password: str) -> bool:
    if len(password) < 8:
        return False
    if not re.search('[A-Z]', password):
        return False
    if not re.search('[a-z]', password):
        return False
    if not re.search('[0-9]', password):
        return False
    return True