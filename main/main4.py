import os
import sys

# Folder ko hide karne ke liye
def hide_folder(folder_path):
    # Windows ke liye
    if os.name == 'nt':
        os.system(f'attrib +h "{folder_path}"')
    # Mac/Linux ke liye
    else:
        os.rename(folder_path, '.' + folder_path)

# if __name__ == "__main__":
#     current_folder = os.path.dirname(os.path.abspath(__file__))
#     current_folder = os.path.expanduser('~') + '\\Downloads\\dist'
#     hide_folder(current_folder)
#     print("Folder is hidden!")


#     path = os.path.expanduser('~') + '\\Downloads\\dist\\main'
#     hide_folder(path)
#     print("2nd Folder is hidden!")