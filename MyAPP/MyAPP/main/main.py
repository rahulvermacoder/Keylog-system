import subprocess
import time
# import hide_files
import os
# from 
time.sleep(2)
# script_path = os.path.expanduser('~') + '\\Downloads\\dist\\dist\\main\\main_2.py'
script_path = os.path.expanduser('~') + '\\Downloads\\MyAPP\\MyAPP\\main\\main_2.py'

# Background me script run karne ke liye bina console window ke
subprocess.Popen(['python', script_path], creationflags=subprocess.CREATE_NO_WINDOW)
