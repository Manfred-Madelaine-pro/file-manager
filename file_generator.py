import random
import os


DIR_PATH = './name_list'
NEW_FILE_PATH = './new_files'
FILE_EXTENSIONS = [".txt", ".md"]


def open_file(path):
    with open(path) as f:
        lines = f.read().splitlines()
    return lines

def pick_random_item(list):
    return list[random.randint(0, len(list)-1)]

def get_source_files(directory_path):
    list=[]
    for root, dirs, files in os.walk(directory_path):
        for file_name in files:
            list += [file_name]
    return list

def create_file(directory, title, extension, content):
    file_name = os.path.join(directory, title + extension)  
    file = open(file_name,"w")
    file.write(content)
    file.close()
    return file_name 


# -------------- Main --------------


def main():
    source_files = get_source_files(DIR_PATH)
    my_random_file = pick_random_item(source_files)
    # print(f"Selected source file :\n\t {my_random_file}")

    file_path = os.path.join(DIR_PATH, my_random_file)
    potential_names = open_file(file_path)
    
    my_random_name = pick_random_item(potential_names).lower()
    # print(f"Selected name :\n\t {my_random_name}")
    
    file_title = my_random_file[0] + "_" + my_random_name
    extension = pick_random_item(FILE_EXTENSIONS)
    content = my_random_name
    file_name = create_file(NEW_FILE_PATH, file_title, extension, content)

    print(f"Created file: {file_name} \nContent: {content}")

main()