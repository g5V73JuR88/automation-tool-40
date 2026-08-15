import os
import json

class ConfigError(Exception):
    pass

def load_config(file_path):
    if not os.path.isfile(file_path):
        raise ConfigError(f'Config file does not exist: {file_path}')
    try:
        with open(file_path, 'r') as file:
            config = json.load(file)
    except json.JSONDecodeError:
        raise ConfigError(f'Invalid JSON in config file: {file_path}')
    except Exception as e:
        raise ConfigError(f'Error reading config file: {file_path}, {str(e)}')
    return config

if __name__ == '__main__':
    config_path = 'path/to/config.json'
    try:
        config = load_config(config_path)
        print(config)
    except ConfigError as ce:
        print(ce)