class CustomError(Exception):
    pass

class ValidationError(CustomError):
    def __init__(self, message):
        super().__init__(message)

class NotFoundError(CustomError):
    def __init__(self, resource):
        self.resource = resource
        message = f'{resource} not found'
        super().__init__(message)

class PermissionDeniedError(CustomError):
    def __init__(self, action):
        self.action = action
        message = f'Permission denied for action: {action}'
        super().__init__(message)

class DatabaseError(CustomError):
    def __init__(self, message):
        super().__init__(message)
