import json
import os

class ConfigLoader:
    def __init__(self, default_config_path='default_config.json', user_config_path='user_config.json'):
        self.default_config = self.load_config(default_config_path)
        self.user_config = self.load_config(user_config_path)
        self.combined_config = self.merge_configs(self.default_config, self.user_config)

    def load_config(self, file_path):
        if not os.path.isfile(file_path):
            return {}
        with open(file_path, 'r') as file:
            return json.load(file)

    def merge_configs(self, default_config, user_config):
        combined = default_config.copy()
        combined.update(user_config)
        return combined

    def get_config(self):
        return self.combined_config
