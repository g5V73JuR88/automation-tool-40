API_URL = 'https://api.example.com'

TIMEOUT = 30

RETRY_COUNT = 3

DEFAULT_HEADERS = {
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}

STATUS_CODES = {
    'success': 200,
    'not_found': 404,
    'server_error': 500
}

LOG_LEVELS = {
    'debug': 'DEBUG',
    'info': 'INFO',
    'warning': 'WARNING',
    'error': 'ERROR',
    'critical': 'CRITICAL'
}

SUPPORTED_FORMATS = ['json', 'xml', 'yaml']