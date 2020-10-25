import os
import json
import datetime


ROOT = 'new_files'
OUTPUT = 'analyzed_output/'
STRUCTURE_NAME = 'analyzed_structure'

DATE_FORMAT = '%Y-%m-%d-%H:%M:%S'


class DirEntry:
    def __init__(self, name, path, type, size, creation_time):
        self.name = name
        self.path = path
        self.type = type
        self.size = size
        self.creation_time = datetime.datetime.fromtimestamp(creation_time).strftime(DATE_FORMAT)

    def __str__(self):
        date_time = self.creation_time
        txt = f'{self.name} (format: {self.type}, size: {self.size} bytes, creation date: {date_time})'
        return txt

def analyze(root):
    properties = retrieve_properties(root)

    create_dir(OUTPUT)
    date = datetime.datetime.today().strftime(DATE_FORMAT)
    dest_name = OUTPUT + '-'.join([STRUCTURE_NAME, root, date]) + '.json'
    convert_to_json(properties, dest_name)

def retrieve_properties(path):
    properties = []
    with os.scandir(path) as it:
        for entry in it:
            dir_entry = map_entry_to_DirEntry(entry)
            properties += [dir_entry]
            if entry.is_dir():
                properties += retrieve_properties(entry.path)

    return properties

def map_entry_to_DirEntry(entry):
    type = 'dir' if entry.is_dir() else entry.name.split('.')[-1]
    return DirEntry(
                entry.name, 
                entry.path, 
                type, 
                entry.stat().st_size,
                entry.stat().st_ctime)

def create_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def convert_to_json(data, destination):
    serialized_data = [vars(d) for d in data]
    with open(destination, 'w', encoding='utf-8') as f:
        json.dump(serialized_data, f, ensure_ascii=False, indent=4)

    print(f"File created at {destination}")


# -------------- Main --------------


def main(): 
   analyze(ROOT)


main()