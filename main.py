import threading
import _tkinter as tk
import pynput.mouse
from pynput.mouse import Listener
import subprocess
import time


# Global variables for overlay and timer
global start_x, start_y, end_x, end_y, is_overlay_active, timer_thread

def create_overlay():
    global overlay

    # Create root window and set transparent background
    overlay = Tk()
    overlay.attributes('-alpha', 0.5)  # Make semi-transparent
    overlay.overrideredirect(True)  # Remove window decorations

    # Set dimensions (fullscreen by default)
    overlay.geometry("+0+0")

    # Start the window in background
    overlay.mainloop(n=0)  # Don't block main script execution
    is_overlay_active = True


def close_overlay():
    global overlay
    overlay.destroy()


def close_overlay_after_timeout():
    global is_overlay_active

    # Wait for 5 seconds
    for _ in range(5):
        if not is_overlay_active:
            return  # Timer cancelled, exit thread
        time.sleep(1)

    # Timeout reached, close the overlay
    close_overlay()

    
def on_click(x, y, button, pressed):
    global start_x, start_y, end_x, end_y, is_overlay_active, timer_thread

    # Check if first click
    if not start_x and not start_y:
        start_x, start_y = x, y
        print("First click at:", x, y)
    # Check if second click (assuming opposite corner)
    else:
        end_x, end_y = x, y
        print("Second click at:", x, y)
        capture_screen(start_x, start_y, end_x, end_y)
        # Cancel the timer thread (if still active)
        is_overlay_active = False
        close_overlay()
        timer_thread.join()


def capture_screen(x1, y1, x2, y2):
    # Use subprocess to call screencapture with appropriate arguments
    subprocess.run(["screencapture", "-l", f"{x1},{y1},{x2},{y2}", "-x", "output.png"])
    # Process or handle the captured image here

# ... other parts of your script (e.g., text extraction from the captured image)

# Create the overlay in a separate thread
# threading.Thread(target=create_overlay).start()


# Start click listener
create_overlay()
with Listener(on_click=on_click) as listener:
    # Start a timer thread
    is_overlay_active = True
    timer_thread = threading.Thread(target=close_overlay_after_timeout)
    timer_thread.start()
    print('listening')
    listener.join()

# Close the overlay after capture (if it wasn't closed already)
if is_overlay_active:
    close_overlay()

