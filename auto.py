from aifc import Error

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import os
import time

folder_from = "D:/test"
folder_to = "D:/test_2"

for f in os.listdir(folder_from):
    src = os.path.join(folder_from, f)
    new_src = os.path.join(folder_to, f)
    try:
        os.rename(src, new_src)
    except:
        print("error in " + f)


# class myHandler(FileSystemEventHandler):
#     def on_modified(self, event):
#         for f in os.listdir(folder_from):
#             src = os.path.join(folder_from, f)
#             new_src = os.path.join(folder_to, f)
#             try:
#                 os.rename(src, new_src)
#             except:
#                 os.remove(src)
#
#
# event_handler = myHandler()
# observer = Observer()
# observer.schedule(event_handler, folder_from, recursive=True)
# observer.start()
#
# try:
#     while True:
#         time.sleep(10)
# except KeyboardInterrupt:
#     observer.stop()
# observer.join()
