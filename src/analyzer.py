import os
import json
import datetime


ROOT = "new_files"
DEST = "data/"
STRUCTURE_NAME = "analyzed_data"

DATE_FORMAT = "%Y-%m-%d-%H:%M:%S"


class DirEntry:
    def __init__(self, name, path, type, size, creation_time):
        self.name = name
        self.path = path
        self.type = type
        self.size = size
        self.creation_time = datetime.datetime.fromtimestamp(creation_time).strftime(
            DATE_FORMAT
        )

    def __str__(self):
        date_time = self.creation_time
        txt = f"{self.name} (format: {self.type}, size: {self.size} bytes, creation date: {date_time})"
        return txt


def analyze(root, dest):
    root_entries = retrieve_entries(root)
    dest_name = prepare_dest_folder(root, dest)
    serialized_data = serialize(root_entries)
    convert_to_json(serialized_data, dest_name)


def retrieve_entries(path):
    entries = []
    with os.scandir(path) as it:
        for entry in it:
            dir_entry = map_entry_to_DirEntry(entry)
            entries += [dir_entry]
            if entry.is_dir():
                entries += retrieve_entries(entry.path)
    return entries


def map_entry_to_DirEntry(entry):
    type = "dir" if entry.is_dir() else entry.name.split(".")[-1]
    return DirEntry(
        entry.name, entry.path, type, entry.stat().st_size, entry.stat().st_ctime
    )


def prepare_dest_folder(root, dest):
    create_dir(dest)
    date = datetime.datetime.today().strftime(DATE_FORMAT)
    dest_name = dest + "-".join([STRUCTURE_NAME, root, date]) + ".json"
    return dest_name


def create_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


def serialize(data):
    return [vars(d) for d in data]


def convert_to_json(data, destination):
    with open(destination, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print(f"File created at {destination}")


# -------------- Main --------------


def main():
    analyze(ROOT, DEST)


main()
