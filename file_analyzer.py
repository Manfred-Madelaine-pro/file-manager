import os
import datetime


ROOT = 'new_files'
DATE_FORMAT = '%Y-%m-%d-%H:%M:%S'

class DirEntry:
    def __init__(self, name, path, type, size, creation_time):
        self.name = name
        self.path = path
        self.type = type
        self.size = size
        self.creation_time = creation_time

    def __str__(self):
        date_time = datetime.datetime.fromtimestamp(self.creation_time).strftime(DATE_FORMAT)
        txt = f'{self.name} (format: {self.type}, size: {self.size} bytes, creation date: {date_time})'
        return txt

def analyze(root):
    # print content
    retreive_properties(root)



def retreive_properties(path):
    properties = []
    with os.scandir(path) as it:
        for entry in it:
            if not entry.name.startswith('.'):
                type = 'dir' if entry.is_dir() else entry.name.split('.')[-1]

                dir_entry = DirEntry(
                                entry.name, 
                                entry.path, 
                                type, 
                                entry.stat().st_size,
                                entry.stat().st_ctime)

                properties += [dir_entry]

    [print(d) for d in properties]
    return properties


# -------------- Main --------------


def main(): 
   analyze(ROOT)

main()