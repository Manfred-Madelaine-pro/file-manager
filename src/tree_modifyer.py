import os
import json
import glob


ROOT = "trees/"
TOKEN = "new"


def modifyer(root):
    latest_file = get_latest_file(root)
    data = load_data(latest_file)
    modifyed_data = modify(data, root)
    file_saver(root, latest_file, modifyed_data)


def get_latest_file(path):
    files = glob.glob(path + "*")
    filtered_files = [f for f in files if f.startswith(TOKEN)]
    return max(files, key=os.path.getctime)


def load_data(json_input):
    with open(json_input) as json_file:
        data = json.load(json_file)
    return data


def modify(data, root):
    for entry in data:
        move(root, entry)
    return data


def move(root, entry):
    path_elements = get_path_elements(root.replace("/", ""), entry)
    entry["path"] = "/".join(path_elements)


# TODO extract type
def get_path_elements(root, entry):
    creation_year = entry["creation_time"].split("-")[0]
    return [root, creation_year, entry["type"], entry["name"]]


def file_saver(path, json_name, data):
    dest_name = json_name.split("/")[-1]
    print(dest_name)
    convert_to_json(data, path + TOKEN + "_" + dest_name)


def convert_to_json(data, destination):
    with open(destination, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print(f"File created at {destination}")


# -------------- Main --------------


def main():
    modifyer(ROOT)


main()