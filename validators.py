import re

def validate_email(email):
    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(regex, email) is not None

def validate_phone(phone):
    regex = r'^(\+\d{1,3}[- ]?)?\d{10}$'
    return re.match(regex, phone) is not None

def validate_url(url):
    regex = r'^(http|https)://[^\s/$.?#].[^\s]*$'
    return re.match(regex, url) is not None

if __name__ == '__main__':
    print(validate_email('test@example.com'))  # True
    print(validate_phone('+1234567890'))  # True
    print(validate_url('https://www.example.com'))  # True