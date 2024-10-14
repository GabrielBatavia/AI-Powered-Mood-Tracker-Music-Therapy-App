# backend/user_data.py

import json
import os

DATA_FILE = 'user_data.json'

class UserDataManager:
    def __init__(self):
        self.data = {}
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, 'r') as f:
                self.data = json.load(f)

    def save_data(self, new_data):
        self.data.update(new_data)
        with open(DATA_FILE, 'w') as f:
            json.dump(self.data, f)

    def get_data(self, key):
        return self.data.get(key, None)
