import random
import os


SOURCE_NAME_DIR = "name_list"
NEW_FILE_DIR = "root"
FILE_EXTENSIONS = [".txt", ".md"]

NB_FILES_TO_CREATE = 10


def open_file(path):
    with open(path) as f:
        lines = f.read().splitlines()
    return lines


def pick_random_item(list):
    return list[random.randint(0, len(list) - 1)]


def get_source_files(directory_path):
    list = []
    for root, dirs, files in os.walk(directory_path):
        for file_name in files:
            list += [file_name]
    return list


def create_file(directory, title, extension, content):
    file_name = os.path.join(directory, title + extension)
    file = open(file_name, "w")
    file.write(content)
    file.close()
    return file_name


def create_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


def create_random_file_from_source_dir(source_dir, file_extensions, destination):
    source_files = get_source_files(source_dir)
    my_random_file = pick_random_item(source_files)

    file_path = os.path.join(source_dir, my_random_file)
    potential_names = open_file(file_path)

    my_random_name = pick_random_item(potential_names).lower()

    file_title = my_random_file[0] + "_" + my_random_name
    extension = pick_random_item(file_extensions)
    content = my_random_name

    create_dir(destination)
    return create_file(destination, file_title, extension, content)


# -------------- Main --------------


def main():
    for i in range(NB_FILES_TO_CREATE):
        file_name = create_random_file_from_source_dir(
            SOURCE_NAME_DIR, FILE_EXTENSIONS, NEW_FILE_DIR
        )
        print(f"File #{i+1}: {file_name}")


main()
