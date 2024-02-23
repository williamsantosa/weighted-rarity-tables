import json
import yaml
import os

def load_json(file_location):
    with open(file_location, 'r') as file:
        data = json.load(file)
    return data

def load_yaml(file_location):
    with open(file_location, 'r') as file:
        data = yaml.safe_load(file)
    return data

def load_tables(file_location):
    # Check if file_location is supplied
    if file_location is None or file_location == '':
        return None
    
    # Check if the file exists and raise an error if it doesn't
    elif not os.path.exists(file_location):
        raise FileNotFoundError(f'File not found: {file_location}')

    # Return loaded data based on file extension
    _, file_extension = os.path.splitext(file_location)
    if file_extension == '.json':
        return load_json(file_location)
    elif file_extension == '.yaml':
        return load_yaml(file_location)
    else:
        raise ValueError(f'Unrecognized file extension: {file_extension}')