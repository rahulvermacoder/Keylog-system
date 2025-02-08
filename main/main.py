import subprocess
import time
# import hide_files
import os
# from 
time.sleep(1)

script_path = os.path.expanduser('~') + '\\Downloads\\dist\\main\\main_2.py'
# Background me script run karne ke liye bina console window ke
subprocess.Popen(['python', script_path], creationflags=subprocess.CREATE_NO_WINDOW)
