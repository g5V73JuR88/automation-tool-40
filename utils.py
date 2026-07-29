import json

def load_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)


def save_json(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


def merge_dicts(dict1, dict2):
    merged = dict1.copy()
    merged.update(dict2)
    return merged


def filter_dict(data, keys):
    return {key: data[key] for key in keys if key in data}


def get_keys(data):
    return list(data.keys())