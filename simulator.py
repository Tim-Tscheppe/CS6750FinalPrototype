import tkinter as tk
from PIL import Image, ImageTk

from water_haptic_feedback import *

class AppleWatchSimulator:
    def __init__(self, root):
        self.root = root
        self.root.title("Apple Watch Simulator")
        self.root.geometry("1600x1400")

        self.current_screen = None

        # Load main watch face image
        self.main_watch_image = self.load_image("images/MainFace.png")
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
        
        water_haptic_feedback()

        water_mode_image = self.load_image("images/WaterMode.png")
        self.current_screen_label.config(image=water_mode_image)
        self.current_screen = water_mode_image
        self.water_mode = True

    def tap_side_crown(self):
        if self.water_mode:
            tap_side_crown_image = self.load_image("images/ExitWaterMode.png")
            self.current_screen_label.config(image=tap_side_crown_image)
            self.current_screen = tap_side_crown_image
            self.root.after(3000, self.return_to_water_face)
    
    def return_to_water_face(self):
        water_mode_image = self.load_image("images/WaterMode.png")
        self.current_screen_label.config(image=water_mode_image)
        self.current_screen = water_mode_image

    def hold_side_crown(self):
        self.current_screen_label.config(image=self.main_watch_image)
        self.water_mode = False

if __name__ == "__main__":
    root = tk.Tk()
    app = AppleWatchSimulator(root)
    root.mainloop()