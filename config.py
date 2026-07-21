import os

class ConfigError(Exception):
    pass

class Config:
    def __init__(self, config_file):
        self.config_file = config_file
        self.settings = self.load_config()

    def load_config(self):
        if not os.path.isfile(self.config_file):
            raise ConfigError(f'Config file {self.config_file} does not exist.')
        try:
            with open(self.config_file, 'r') as file:
                return self.parse_config(file)
        except IOError as e:
            raise ConfigError(f'Error reading config file: {e}')

    def parse_config(self, file):
        settings = {}
        for line in file:
            if line.strip() and not line.startswith('#'):
                key, value = line.split('=', 1)
                settings[key.strip()] = value.strip()
        return settings

    def get(self, key, default=None):
        return self.settings.get(key, default)

    def set(self, key, value):
        self.settings[key] = value
