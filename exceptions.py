class CustomError(Exception):
    pass

class ValidationError(CustomError):
    def __init__(self, message):
        super().__init__(message)

class DataProcessingError(CustomError):
    def __init__(self, message):
        super().__init__(message)

class ConfigurationError(CustomError):
    def __init__(self, message):
        super().__init__(message)

class NotFoundError(CustomError):
    def __init__(self, resource):
        message = f'{resource} not found'
        super().__init__(message)