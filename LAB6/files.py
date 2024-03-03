#1
import os

def files(path):
    d = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    f = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    
    print("Directories:")
    print(d)
    
    print("\nFiles:")
    print(f)
    
    print("\nAll Directories and Files:")
    print(os.listdir(path))

path = "C:"
files(path)

#2
import os

def check(path):
    if os.path.exists(path):
        print(f"The path {path} exists.")

        if os.access(path, os.R_OK):
            print("Readable")
        else:
            print("Not readable")

        if os.access(path, os.W_OK):
            print("Writable")
        else:
            print("Not writable")

        if os.access(path, os.X_OK):
            print("Executable")
        else:
            print("Not executable")

    else:
        print(f"The path {path} does not exist.")

path = "C:"
check(path)

#3
import os

def check_path(path):
    if os.path.exists(path):
        print(f"The path {path} exists.")
        head, tail = os.path.split(path)
        print(f"Directory: {head}")
        print(f"File name: {tail}")
    else:
        print(f"The path {path} does not exist.")

path_to_check = "C:/Users/user/Desktop/first-1/LAB6/1.txt"
check_path(path_to_check)

#4
def count(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            print(f"Number of lines in {file_path}: {len(lines)}")
    except FileNotFoundError:
        print(f"File {file_path} not found.")

path = "C:/Users/user/Desktop/first-1/LAB6/1.txt"
count(path)

#5
def write(path, list):
    with open(path, 'w') as file:
        for item in list:
            file.write(str(item) + '\n')

path = "C:/Users/user/Desktop/first-1/LAB6/1.txt"
list = [1, 2, 3, 4, 5]
write(path, list)

#6
import string

def create():
    for l in string.ascii_uppercase:
        file_name = f"{l}.txt"
        with open(file_name, 'w') as file:
            file.write(f"This is file {l}")

create()

#7
with open('1.txt', 'r') as path1, open('2.txt', 'a') as path2:
    for line in path1:
        path2.write(line)

#8
def delete(path):
    if os.path.exists(path):
        os.remove(path)
        print(f"File {path} deleted successfully.")
    else:
        print(f"File {path} not found.")

file = "C:/Users/user/Desktop/first-1/LAB6/1.txt"
delete(file)
