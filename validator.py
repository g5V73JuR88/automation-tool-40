import re

class InputValidator:
    @staticmethod
    def validate_email(email):
        regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(regex, email) is not None

    @staticmethod
    def validate_age(age):
        return isinstance(age, int) and 0 < age < 120

    @staticmethod
    def validate_user_input(email, age):
        if not InputValidator.validate_email(email):
            raise ValueError('Invalid email address')
        if not InputValidator.validate_age(age):
            raise ValueError('Invalid age')

if __name__ == '__main__':
    email = input('Enter your email: ')
    age = int(input('Enter your age: '))
    try:
        InputValidator.validate_user_input(email, age)
        print('Input is valid')
    except ValueError as e:
        print(e)