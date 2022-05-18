from pynput import mouse
from pynput.keyboard import Key, Listener
import ctypes
import sys


def on_press(key):
    ctypes.windll.user32.LockWorkStation()
    key_listener.stop()
    listener.stop()
    sys.exit()


from pynput import keyboard
key_listener = keyboard.Listener(on_press=on_press)
key_listener.start()


def on_move(x, y):
    ctypes.windll.user32.LockWorkStation()
    key_listener.stop()
    listener.stop()
    sys.exit()
    
with mouse.Listener(on_move=on_move) as listener:
    listener.join()

