import json

class JSONFileHandler:
    def __init__(self, filename):
        self.filename = filename

    def read_json(self):
        try:
            with open(self.filename, 'r') as json_file:
                data = json.load(json_file)
            return data
        except FileNotFoundError:
            return "File not found"
        except Exception as e:
            return str(e)

    def write_json(self, data, indent=None):
        try:
            with open(self.filename, 'w') as json_file:
                json.dump(data, json_file, indent=indent)
            return "File written successfully"
        except Exception as e:
            return str(e)
