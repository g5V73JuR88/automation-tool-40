import os
from datetime import datetime


def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)


def timestamp():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')


def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()


def write_file(file_path, data):
    with open(file_path, 'w') as file:
        file.write(data)


def append_to_file(file_path, data):
    with open(file_path, 'a') as file:
        file.write(data)


def list_files(directory):
    return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
