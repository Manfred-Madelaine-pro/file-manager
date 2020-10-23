import os


ROOT = 'new_files'


def analyze(root):
    # print content
    # test(root)
    get_properties(root)

     # gather infos

    # include directories

def test(directory_path):
    for root, dirs, files in os.walk(directory_path):
        for file_name in files:
            # list += [file_name]
            print(file_name)

def get_properties(path):
    with os.scandir(path) as it:
        for entry in it:
            if not entry.name.startswith('.'):
                print(entry.name)
                print(entry.stat())


# -------------- Main --------------


def main(): 
   analyze(ROOT)

main()