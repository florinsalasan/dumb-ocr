import threading
from tkinter import *
import pynput
from pynput import mouse
import subprocess
import time


global overlay
global count
count = 0


def create_overlay():
    global is_overlay_active
    global overlay

    # Create root window and set transparent background
    overlay = Tk()
    screen_width = overlay.winfo_screenwidth()
    screen_height = overlay.winfo_screenheight()
    overlay.geometry('{0}x{1}'.format(str(screen_width), str(screen_height)))
    print(screen_width, screen_height)
    overlay.attributes("-alpha", 0.5)
    overlay.wm_attributes('-topmost', 1)
    overlay.bg = Canvas(overlay, width=screen_width, height=screen_height, bg='white')
    overlay.bg.pack()
    overlay.mainloop()

    print("overlay active")
    is_overlay_active = True
    close_overlay_after_timeout(overlay)
    listener = mouse.Listener(
        on_move=on_move,
        on_click=on_click)
    listener.start()


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
    print('about to stop inside timeout function')
    pynput.mouse.Listener.stop


def on_move(x, y):
    print("Pointer moved to {0}".format((x, y)))


def on_click(x, y, button, pressed):
    global pressed_location
    global released_location
    print(pressed)
    if pressed:
        pressed_location = x, y
    else:
        released_location = x, y
        print('You pressed at {0}x{1} and released at {2}x{3}'.format(*pressed_location, *released_location))


create_overlay()
