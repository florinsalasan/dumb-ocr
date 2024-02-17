import tkinter as tk
from PIL import Image
from PIL import ImageGrab


class Selector:

    def __init__(self, root):
        self.root = root

        self.screen_height = root.winfo_screenheight()
        self.screen_width = root.winfo_screenwidth()
        self.canvas = tk.Canvas(root, width=self.screen_width, height=self.screen_height, bg='white')
        self.canvas.pack()

        self.root.attributes('-alpha', 0.4)

        self.canvas.bind("<ButtonPress-1>", self.start_draw)
        self.canvas.bind("<ButtonRelease-1>", self.stop_draw)

        self.drawing = False
        self.start_x, self.start_y = None, None

        self.coords = {
            'start_x': None,
            'start_y': None,
            'stop_x': None,
            'stop_y': None,
        }
        self.rectangles = []

    def start_draw(self, event):
        self.drawing = True
        self.start_x, self.start_y = event.x, event.y

    def stop_draw(self, event):
        if self.drawing:
            end_x, end_y = event.x, event.y
            rectangle = self.canvas.create_rectangle(
                self.start_x, self.start_y, end_x, end_y, outline="black", width=1,
            )
            self.drawing = False
            self.coords['start_x'] = self.start_x
            self.coords['start_y'] = self.start_y
            self.coords['stop_x'] = end_x
            self.coords['stop_y'] = end_y
            self.rectangles.append(self.coords)
            self.root.destroy()


if __name__ == '__main__':
    root = tk.Tk()
    app = Selector(root)
    root.mainloop()
    print(app.rectangles)

    # ImageGrab bbox is left, top, right, bottom values
    ig_top = min(app.rectangles[0]['start_y'], app.rectangles[0]['stop_y'])
    ig_bottom = max(app.rectangles[0]['start_y'], app.rectangles[0]['stop_y'])
    ig_left = min(app.rectangles[0]['start_x'], app.rectangles[0]['stop_x'])
    ig_right = max(app.rectangles[0]['start_x'], app.rectangles[0]['stop_x'])

    # get the image using ImageGrab
    selected_area = ImageGrab.grab(bbox=(ig_left, ig_top, ig_right, ig_bottom))
    selected_area.save('ss.png')
