import os
import shutil
import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:\\Users\\Admin\\Downloads"
to_dir = "C:\\Users\\Admin\\Documents"


list_of_files = os.listdir(from_dir)
print(list_of_files)

for file_name in list_of_files:
    root,ext = os.path.splitext(file_name)

    if ext == "" :
        continue
    
    if ext in [".txt", ".doc", ".docx", ".pdf"]:
        path1 = from_dir + '/' + file_name
        path2 = to_dir + '/' + "Document_Files"
        path3 = to_dir + '/' + "Document_Files" + '/' + file_name

        if os.path.exists(path2):
            print("Moving " + file_name + "..")
            shutil.move(path1, path3)

        else:
            os.makedirs(path2)
            print("Moving "+ file_name + "..")
            shutil.move(path1, path3)

class FileEventHandler(FileSystemEventHandler):

    def on_created(self, event):
        print(f"Hey, {event.srcz_path} has been created!")

    def on_deleted(self, event):
        print(f"Oops! Someone deleted {event.src_path}!")

try:
    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt:
    print("stopped!")
    Observer.stop()  
