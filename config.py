import os
import json

class ConfigError(Exception):
    pass

class Config:
    def __init__(self, config_file):
        self.config_file = config_file
        self.config_data = self.load_config()

    def load_config(self):
        if not os.path.isfile(self.config_file):
            raise ConfigError('Configuration file not found')
        try:
            with open(self.config_file, 'r') as file:
                data = json.load(file)
            return data
        except json.JSONDecodeError as e:
            raise ConfigError(f'Error decoding JSON: {e}')
        except Exception as e:
            raise ConfigError(f'Unexpected error: {e}')

    def get(self, key, default=None):
        return self.config_data.get(key, default)

    def set(self, key, value):
        self.config_data[key] = value
        self.save_config()

    def save_config(self):
        try:
            with open(self.config_file, 'w') as file:
                json.dump(self.config_data, file, indent=4)
        except Exception as e:
            raise ConfigError(f'Error saving configuration: {e}')