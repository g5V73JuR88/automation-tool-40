def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()


def write_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)


def append_to_file(file_path, content):
    with open(file_path, 'a') as file:
        file.write(content)


def process_data(data, func):
    return [func(item) for item in data]


def calculate_average(numbers):
    return sum(numbers) / len(numbers) if numbers else 0


def filter_even_numbers(numbers):
    return [num for num in numbers if num % 2 == 0]


def find_max_value(numbers):
    return max(numbers) if numbers else None


def find_min_value(numbers):
    return min(numbers) if numbers else None
