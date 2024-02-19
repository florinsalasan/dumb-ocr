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
        print(self.screen_width, self.screen_height)
        # Used image grab to see what the real resolution of my screen was,
        # noticed it was twice what tk was reporting so I scaled the self.coords
        # by 2 and now it is grabbing the matching selected area by the user.
        img = ImageGrab.grab()
        self.size = img.size
        print('above is screen_width, below is self.size')
        print(self.size)
        self.width_ratio = self.size[0] / self.screen_width
        self.height_ratio = self.size[1] / self.screen_height
        print(self.width_ratio, self.height_ratio)

        self.root.attributes('-alpha', 0.2)

        self.canvas.config(width=self.screen_width, height=self.screen_height)

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
            self.canvas.create_rectangle(
                self.start_x, self.start_y, end_x, end_y, outline="black", width=1,
            )
            self.drawing = False
            self.coords['start_x'] = self.start_x * self.width_ratio
            self.coords['start_y'] = self.start_y * self.height_ratio
            self.coords['stop_x'] = end_x * self.width_ratio
            self.coords['stop_y'] = end_y * self.height_ratio
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
    print(ig_top, ig_bottom, ig_left, ig_right)
    selected_area.save('ss.png')
