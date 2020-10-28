import os
import json
import glob


JSON_FILE_PATH = 'json_structure_analyzed/'
OUTPUT = 'json_modifyed_files'


def select_latest_json_file(path): #OK
    list_of_files = glob.glob(path + '/*')
    latest_file = max(list_of_files, key = os.path.getctime)#.split(path)[1]
    return latest_file

def json_modifyer(json_file_path, structured_folder, latest_json_file): #
    selected_json_file = latest_json_file
    file_list = []
    with open(selected_json_file) as json_file:
        data = json.load(json_file)
    for entry in data:
        entry["path"] = structured_folder + "/" + entry["creation_time"].split("-")[0] + \
        "/" + entry["type"] + "/" + entry["name"]
    return data

def file_saver(path,json_name,data):
    create_dir(path)
    dest_name = json_name.replace('json_structure_analyzed/analyzed_structure',\
        path + '/updated_structure')
    print(dest_name, '\n', path)
    convert_to_json(data, dest_name)

def create_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def convert_to_json(data, destination):
    with open(destination, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    print(f"File created at {destination}")


# -------------- Main --------------


def main():
    latest_json_file = select_latest_json_file(JSON_FILE_PATH)
    modifyed_data = json_modifyer(JSON_FILE_PATH, OUTPUT, latest_json_file)
    file_saver(OUTPUT, latest_json_file,modifyed_data)
main()
