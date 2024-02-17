import tkinter as tk


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
            print(end_x, end_y)
            rectangle = self.canvas.create_rectangle(
                self.start_x, self.start_y, end_x, end_y, outline="black", width=1,
            )
            self.rectangles.append(rectangle)
            self.drawing = False
            self.coords['start_x'] = self.start_x
            self.coords['start_y'] = self.start_y
            self.coords['stop_x'] = end_x
            self.coords['stop_y'] = end_y
            print(self.coords)


if __name__ == '__main__':
    root = tk.Tk()
    app = Selector(root)
    root.mainloop()
