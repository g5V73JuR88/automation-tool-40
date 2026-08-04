import json

class ConfigLoader:
    def __init__(self, default_config):
        self.default_config = default_config
        self.config = default_config.copy()

    def load(self, filepath):
        try:
            with open(filepath, 'r') as file:
                file_config = json.load(file)
                self.config.update(file_config)
        except FileNotFoundError:
            pass
        except json.JSONDecodeError:
            raise ValueError('Invalid JSON format in config file.')

    def get(self, key, default=None):
        return self.config.get(key, default)

# Example of default configuration
DEFAULT_CONFIG = {
    'setting_1': 'default_value_1',
    'setting_2': True,
    'setting_3': 42
}

# Usage:
# config_loader = ConfigLoader(DEFAULT_CONFIG)
# config_loader.load('config.json')
# setting_value = config_loader.get('setting_1')