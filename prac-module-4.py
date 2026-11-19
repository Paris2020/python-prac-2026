import os
import shutil
from pathlib import Path
from datetime import datetime

#Listing files and directories
root_path = os.path.join("/","users","username")
print(root_path)

root_path = os.getcwd()
print(root_path)

os.chdir("/home")
root_path = os.getcwd()
print(root_path)

print()
print("============= END: OS tasks ================")
print()


root_path = "/Users/nellymoseki/git/tutorials/python-prac-2026"
for current, subdirectories, files in os.walk(root_path):
    print("Current directory: ", current)
    for current_subdir in subdirectories:
        print("Current subdirectory: ", current_subdir)
    for current_file in files:
        print("File: ", current_file)
    print()


print()
print("----------------------------")
print()


#Listing files and directories (continued)
def contents(current_path):
    print(current_path)

    for current, subdirectories, files in os.walk(current_path):
        subdirectories.sort()
        files.sort()

        for current_subdir in subdirectories:
            next_path = os.path.join(current_path, current_subdir)
            if os.path.exists(next_path):
                contents(next_path)

        for current_file in files:
            full_file_path = os.path.join(current_path, current_file)

            if os.path.exists(full_file_path):
                print("File: ", full_file_path)

root_path = "/Users/nellymoseki/git/tutorials/python-prac-2026"
contents(root_path)


print()
print("----------------------------")
print()

entries = os.listdir("/Users/nellymoseki/git/tutorials/python-prac-2026")
for entry in entries:
    print(entry)

print()

entries = os.scandir("/Users/nellymoseki/git/tutorials")
for entry in entries:
    print(entry)

print()

entries = Path("/Users/nellymoseki/git/tutorials")
for entry in entries.iterdir():
    print(entry)



#Directory operations
root_path = "/Users/nellymoseki/git/tutorials"
#os.mkdir(root_path + "/new-folder")
#os.makedirs(root_path + "/new-folder/sub-dir")
#os.rmdir(root_path + "/new-folder/sub-dir")
#shutil.rmtree(root_path + "/new-folder")
print(root_path)

print()

#File operations
#hutil.move("/Users/nellymoseki/git/tutorials/new-folder-b/mean-girl-energy.jpeg", "/Users/nellymoseki/git/tutorials/new-folder-a/mean-girl-energy.jpeg")
#shutil.copy("/Users/nellymoseki/git/tutorials/new-folder-b/mean-girl-energy.jpeg", "/Users/nellymoseki/git/tutorials/new-folder-a/mean-girl-energy.jpeg")
#os.rename("/Users/nellymoseki/git/tutorials/new-folder-b/mean-girl-energy.jpeg", "/Users/nellymoseki/git/tutorials/new-folder-a/mean-girl-energy.jpeg")

print()

results = os.stat("/Users/nellymoseki/git/tutorials/new-folder-b/mean-girl-energy.jpeg")
print(results)
print()
print("Size: {} bytes".format(results.st_size))
print("Created: {}".format(datetime.fromtimestamp(results.st_mtime)))
print("Accessed: {}".format(datetime.fromtimestamp(results.st_atime)))
print("Modified: {}".format(datetime.fromtimestamp(results.st_mtime)))


