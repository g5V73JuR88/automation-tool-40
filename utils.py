import json

def read_json_file(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)


def write_json_file(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


def merge_dicts(dict1, dict2):
    merged = dict1.copy()
    merged.update(dict2)
    return merged


def filter_dict_by_keys(data_dict, keys):
    return {k: data_dict[k] for k in keys if k in data_dict}


def pretty_print_json(data):
    print(json.dumps(data, indent=4))