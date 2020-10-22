import random

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
    path = './fruits_list.txt'
    fruits = open_file(path)

    # [print(f) for f in fruits]


    print(pick_random_item(fruits))




main()