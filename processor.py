import json
import requests

class DataProcessor:
    def __init__(self, url):
        self.url = url

    def fetch_data(self):
        response = requests.get(self.url)
        response.raise_for_status()
        return response.json()

    def process_data(self, data):
        return [item['value'] for item in data if 'value' in item]

    def save_to_file(self, data, filename):
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)

    def run(self, filename):
        data = self.fetch_data()
        processed_data = self.process_data(data)
        self.save_to_file(processed_data, filename)

if __name__ == '__main__':
    processor = DataProcessor('https://api.example.com/data')
    processor.run('output.json')