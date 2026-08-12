import time
import requests
from functools import wraps


def retry(retries=3, delay=1, backoff=2):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            current_delay = delay
            for attempt in range(retries):
                try:
                    return func(*args, **kwargs)
                except requests.exceptions.RequestException as e:
                    if attempt < retries - 1:
                        time.sleep(current_delay)
                        current_delay *= backoff
                    else:
                        raise e
        return wrapper
    return decorator


@retry(retries=5, delay=2)
def fetch_data(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.json()
