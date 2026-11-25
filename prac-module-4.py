import os
import shutil
import zipfile
import schedule
import requests
import time
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

print()
print("============= END: File operations ================")
print()


#Compressed files

root_path = "/Users/nellymoseki/git/tutorials/"
#with zipfile.ZipFile(root_path + "/new-folder-b.zip", 'r') as zipfile:
    #for current in zipfile.namelist():
        #print(current)

#with zipfile.ZipFile(root_path + "/new-folder-b.zip", 'r') as zip_archive:
    #file_info = zip_archive.getinfo("__MACOSX/new-folder-b/._mean-girl-energy.jpeg")
    #print("File size: {} bytes".format(file_info.file_size))
    #print("Compressed size: {} bytes".format(file_info.compress_size))
    #print("Last modified: {}".format(file_info.date_time))

#with zipfile.ZipFile(root_path + "/new-folder-b.zip", 'r') as zip_archive:
    #zip_archive.extract("__MACOSX/new-folder-b/._mean-girl-energy.jpeg", path=root_path)
    #zip_archive.extractall(root_path + "/new-folder-b")

#with zipfile.ZipFile(root_path + "/new-folder-b.zip", 'w') as zip_archive:
    #zip_archive.write(root_path + "/afrihost-walk-in.png")

#with zipfile.ZipFile(root_path + "/new-folder-b.zip", 'a') as zip_archive:
    #zip_archive.write(root_path + "/poster-1-willow-view.png")


print()
print("============= END: Compressed files ================")
print()


#Scheduling tasks
def display_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Current time: {}".format(current_time))

def display_random_time():
    print("Randomly called - ", end="")
    display_time()

def daily():
    print("It's a new day")

def tuesday_time():
    print("It's 10:19 on Tuesday")

schedule.every(30).seconds.do(display_time)
schedule.every().day.at("08:00").do(daily)
schedule.every().tuesday.at("12:00").do(display_random_time)

continue_loop = False

try:
    while continue_loop:
        schedule.run_pending()
        time.sleep(1)
except:
    continue_loop = False
    print("Schedule ended")


print()
print("============= END: Scheduling tasks ================")
print()


#Making requests
response = requests.get("https://catfact.ninja/fact")
print(response.text)

response = requests.get("https://randomuser.me/api/")
print(response.text)

api_key = "YOUR_API_KEY"
url = "https://api.thedogapi.com/v1/breeds/search"
headers = {"X-Api-Key": api_key}
params = {"q": "pomeranian"}
response = requests.get(url, headers=headers, params=params, timeout=10)

print(response.text)
print(response.headers)
print(response.status_code)
print(response.reason)
print(response.request)
print(response.request.url)
print(response.request.path_url)
print(response.request.method)
print(response.request.headers)

print()
print("============= END: Making requests ================")
print()