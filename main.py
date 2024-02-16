import threading
from tkinter import *
import pynput
from pynput import mouse
import subprocess
import time


def get_x_and_y(event):
    global lasx, lasy
    lasx, lasy = event.x, event.y


def draw_smth(event):
    global lasx, lasy
    canvas.create_rectangle((lasx, lasy, event.x, event.y),
                            fill='red',
                            width=1)
    lasx, lasy = event.x, event.y

# Create root window and set transparent background
overlay = Tk()
screen_width = overlay.winfo_screenwidth()
screen_height = overlay.winfo_screenheight()
overlay.geometry('{0}x{1}'.format(str(screen_width), str(screen_height)))
print(screen_width, screen_height)
overlay.attributes("-alpha", 0.5)
canvas = Canvas(overlay, width=screen_width, height=screen_height, bg='white')
canvas.pack(anchor="nw", fill="both", expand=1)

canvas.bind("<Button-1>", get_x_and_y)
canvas.bind("<B1-Motion>", draw_smth)

overlay.mainloop()
