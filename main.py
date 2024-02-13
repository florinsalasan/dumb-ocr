import threading
from tkinter import *
import pynput
from pynput import mouse
import subprocess
import time


global overlay

def create_overlay():
    global is_overlay_active

    # Create root window and set transparent background
    overlay = Tk()
    screen_width = overlay.winfo_screenwidth()
    screen_height = overlay.winfo_screenheight()
    overlay.geometry(str(screen_width) + 'x' + str(screen_height))
    print(screen_width, screen_height)
    overlay.attributes("-alpha", 0.6)

    print("overlay active")
    is_overlay_active = True
    listener = mouse.Listener(
        on_move=on_move,
        on_click=on_click)
    listener.start()
    close_overlay_after_timeout(overlay)


def close_overlay(overlay):
    overlay.destroy()


def close_overlay_after_timeout(overlay):
    print("timer started")
    global is_overlay_active

    # Wait for 5 seconds
    for _ in range(5):
        if not is_overlay_active:
            return  # Timer cancelled, exit thread
        time.sleep(1)

    # Timeout reached, close the overlay
    close_overlay(overlay)
    pynput.mouse.Listener.stop


def on_move(x, y):
    print("Pointer moved to {0}".format((x, y)))


def on_click(x, y, button, pressed):
    print("{0} at {1}".format(
          'Pressed' if pressed else 'Released', (x, y)))
    if not pressed:
        return False



create_overlay()



