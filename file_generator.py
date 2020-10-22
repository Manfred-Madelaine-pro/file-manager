import random
import os


DIR_PATH = './name_list'


def open_file(path):
    with open(path) as f:
        lines = f.read().splitlines()
    return lines

def pick_random_item(list):
    return list[random.randint(0, len(list)-1)]

def get_source_files(directory_path):
    list=[]
    for root, dirs, files in os.walk(directory_path):
        for filename in files:
            list += [filename]  
    return list


# -------------- Main --------------


def main():
    source_files = get_source_files(DIR_PATH)
    my_random_file = pick_random_item(source_files)
    print(f"Selected source file :\n\t {my_random_file}")

    file_path = DIR_PATH + "/" + my_random_file
    potential_names = open_file(file_path)
    
    my_random_name = pick_random_item(potential_names)
    print(f"Selected name :\n\t {my_random_name}")

    return potential_names

main()