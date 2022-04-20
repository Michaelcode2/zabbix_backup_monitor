
import os

def run_fast_scandir(folder):
    for currentpath, folders, files in os.walk(folder):
        #print(currentpath)
        #print(folders)
        #print(files)
        for file in files:
            print(os.path.join(currentpath, file))

def scandir(folder):

    subfolders = []
    files = []

    for f in os.scandir(folder):
        if f.is_dir():
            subfolders.append(f.name)
        if f.is_file():
            if os.path.splitext(f.name)[1].lower() in folder:
                files.append(f.path)

    return subfolders, files

folder = os.path.dirname(os.path.realpath(__file__))
print(folder)
subfolders, files = scandir(folder)

print(subfolders)
print(files)
