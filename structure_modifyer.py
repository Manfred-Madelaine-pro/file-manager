import os
import json
import glob
import datetime


JSON_FILE_PATH = 'analyzed_output/'
STRUCTURED_FOLDER = 'structured_folder'


def list_file_generator(json_file_path): #OK
    selected_json_file = select_latest_json_file(json_file_path)
    file_list = []

    with open(selected_json_file) as json_file:
        for line in json_file:
            if '"name":' in line :
                file_list += [line.split('        "name": "')[1].split('",\n')[0]]
    print(file_list, "\n")
    return file_list


def select_latest_json_file(path): #OK
    list_of_files = glob.glob(path + '/*')
    latest_file = max(list_of_files, key = os.path.getctime)#.split(path)[1]
    print(latest_file, '\n')
    return latest_file

def folders_to_create(list_files): #OK
    extensions_list = []
    for file in list_files:
        extensions_list += [file.split(".")[-1]]
    extensions_list = list(set(extensions_list))
    print(extensions_list, "\n")
    return extensions_list

# def create_structured_folder(structured_folder_name,folders_names, list_files):
#     structured_folder_exist = 0
#     if not os.path.exists(structured_folder_name):
#         os.makedirs(structured_folder_name)
#     else :
#         structured_folder_exist = 1
#     for folder in folders:
#         if structured_folder_exist == 0:
#             os.mkdir(structured_folder_name + "/" + folder)
#     for file in list_files:


# to do : 
#get full files dir; not name to change it with 
# os.rename("path/to/current/file.foo", "path/to/new/destination/for/file.foo")

# -------------- Main --------------


def main(): 
   list_files = list_file_generator(JSON_FILE_PATH)
   dirs = folders_to_create(list_files)
   # create_structured_folder(STRUCTURED_FOLDER,dirs,list_files)
main()
