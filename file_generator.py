import random
import os
# open list file
# read the content 
# pick random name
# create a file with the name 
# save content in it 


def open_file(path):
    with open(path) as f:
        lines = f.read().splitlines()
    return lines

def pick_random_item(list):
    return list[random.randint(0, len(list))]

def main():
    list=[]
    path = './name_list'
    for root, dirs, files in os.walk(path):
        for filename in files:
            list += [filename]  
    my_random_file = list[random.randint(0, len(list)-1)]
    print(my_random_file)
    my_random_file_path = open_file(path+"/"+my_random_file)
    print(my_random_file_path)
    return my_random_file_path

main()