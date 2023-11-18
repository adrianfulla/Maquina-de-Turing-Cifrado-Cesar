import json

class JsonOperator():
    def readJson(self, filename):
        try:
            with open(filename, 'r') as json_file:
                data = json.load(json_file)
                return data
        except FileNotFoundError:
            print(f"File '{filename}' not found. Please make sure the file exists.")
        except json.JSONDecodeError:
            print(f"Error decoding JSON in file '{filename}'. Please check the file format.")