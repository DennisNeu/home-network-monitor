import json
import os


class DataHandler:
    """A class that handles saving and loading data from a JSON file."""
    def __init__(self, filename: str):
        """Simple init"""
        self.data = []
        self.filename = filename
        self.load_data()

    def load_data(self):
        """Load data from a JSON file."""
        if os.path.exists(self.filename):
            with open(self.filename, 'r', encoding="utf-8") as file:
                self.data = json.load(file)
        else:
            self.data = []

    def save_data(self, new_data):
        """Save data to a JSON file."""
        with open(self.filename, 'w', encoding="utf-8") as file:
            json.dump(new_data, file, indent=4)

    def delete_data(self):
        """Delete the JSON file."""
        if os.path.exists(self.filename):
            os.remove(self.filename)
            self.data = []