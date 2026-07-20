import json

def read_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data


def write_json(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


def merge_data(source_data, new_data):
    if isinstance(source_data, dict) and isinstance(new_data, dict):
        source_data.update(new_data)
    return source_data


def filter_data(data, keys):
    return {key: data[key] for key in keys if key in data}


# Example usage:
# if __name__ == '__main__':
#     data = read_json('input.json')
#     new_data = {'key': 'value'}
#     merged_data = merge_data(data, new_data)
#     write_json('output.json', merged_data)