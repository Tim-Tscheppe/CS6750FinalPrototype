import tkinter as tk
from PIL import Image, ImageTk

class AppleWatchSimulator:
    def __init__(self, root):
        self.root = root
        self.root.title("Apple Watch Simulator")
        self.root.geometry("400x300")

        self.current_screen = None

        # Load main watch face image
        self.main_watch_image = self.load_image("images/main_watch_face.png")
        self.current_screen_label = tk.Label(root, image=self.main_watch_image)
        self.current_screen_label.pack()

        # Buttons
        self.enter_water_button = tk.Button(root, text="Enter Water Mode", command=self.enter_water_mode)
        self.enter_water_button.pack()

        self.tap_crown_button = tk.Button(root, text="Tap Side Crown", command=self.tap_side_crown)
        self.tap_crown_button.pack()

        self.hold_crown_button = tk.Button(root, text="Hold Side Crown", command=self.hold_side_crown)
        self.hold_crown_button.pack()

    def load_image(self, path):
        return ImageTk.PhotoImage(Image.open(path))

    def enter_water_mode(self):
        # Load water mode image
        water_mode_image = self.load_image("images/water_mode.png")
        self.current_screen_label.config(image=water_mode_image)
        self.current_screen = water_mode_image

    def tap_side_crown(self):
        # TODO: Get this to only work if water mode is active
        tap_side_crown_image = self.load_image("images/tap_side_crown.png")
        self.current_screen_label.config(image=tap_side_crown_image)
        self.root.after(5000, lambda: self.return_to_water_mode(self.current_screen))

    def return_to_water_mode(self, previous_image):
        self.current_screen_label.config(image=previous_image)

    def hold_side_crown(self):
        # Load main watch face image
        self.current_screen_label.config(image=self.main_watch_image)

if __name__ == "__main__":
    root = tk.Tk()
    app = AppleWatchSimulator(root)
    root.mainloop()