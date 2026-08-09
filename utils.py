import time
import requests

class NetworkError(Exception):
    pass

def retry(func, retries=3, delay=2):
    for i in range(retries):
        try:
            return func()
        except NetworkError:
            if i < retries - 1:
                time.sleep(delay)
            else:
                raise

def fetch_data(url):
    response = requests.get(url)
    if response.status_code != 200:
        raise NetworkError('Failed to fetch data')
    return response.json()

if __name__ == '__main__':
    url = 'https://api.example.com/data'
    data = retry(lambda: fetch_data(url))
    print(data)