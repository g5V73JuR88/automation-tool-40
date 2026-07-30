import time
from functools import lru_cache

@lru_cache(maxsize=128)
def complex_calculation(x):
    time.sleep(2)  # Simulates an expensive computation
    return x + x * 2

def process_data(data):
    results = []
    for item in data:
        result = complex_calculation(item)
        results.append(result)
    return results

if __name__ == '__main__':
    data = range(10)
    start_time = time.time()
    output = process_data(data)
    end_time = time.time()
    print(f'Results: {output}')
    print(f'Execution time: {end_time - start_time} seconds')