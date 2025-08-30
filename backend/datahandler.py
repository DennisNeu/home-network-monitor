import json, os

class Datahandler:
    def __init__(self, filename: str):
        self.data = []
        self.filename = filename
        self.load_data()
            
    def load_data(self):
        """Load data from a JSON file."""
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                self.data = json.load(file)
        else:
            self.data = []

    def save_data(self, new_data):
        with open(self.filename, 'w') as file:
            json.dump(new_data, file, indent=4)