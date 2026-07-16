import json
import os

class FileProcessor:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_file(self):
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f'File not found: {self.file_path}')
        if not self.file_path.endswith('.json'):
            raise ValueError('File must be a JSON file.')
        with open(self.file_path, 'r') as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                raise ValueError('File contains invalid JSON.')

    def write_file(self, data):
        if not isinstance(data, dict):
            raise TypeError('Data must be a dictionary.')
        with open(self.file_path, 'w') as file:
            json.dump(data, file, indent=4)

# Example usage:
# processor = FileProcessor('data.json')
# data = processor.read_file()
# processor.write_file(data)