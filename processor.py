import json

class DataProcessor:
    def __init__(self, data):
        self.data = data

    def process(self):
        self.cleanup()
        self.reorganize()

    def cleanup(self):
        self.data = [item for item in self.data if self._is_valid(item)]

    def reorganize(self):
        self.data.sort(key=lambda x: x['name'])

    def _is_valid(self, item):
        return isinstance(item, dict) and 'name' in item

    def to_json(self):
        return json.dumps(self.data)

# Example usage:
if __name__ == '__main__':
    sample_data = [
        {'name': 'Alice', 'age': 30},
        {'name': 'Bob', 'age': 25},
        {'age': 20},
        {'name': 'Eve', 'age': 22}
    ]
    processor = DataProcessor(sample_data)
    processor.process()
    print(processor.to_json())