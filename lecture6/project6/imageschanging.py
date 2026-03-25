import tkinter as tk
from itertools import cycle
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Image Shower")

# 1. Setup your paths
image_paths = [
    r"c:\Users\BUZZ TECH\OneDrive\Pictures\Camera Roll\khubauib.jpg",
    r"c:\Users\BUZZ TECH\OneDrive\Pictures\Camera Roll\student back .jpg",
    r"c:\Users\BUZZ TECH\OneDrive\Pictures\Camera Roll\WIN_20260225_09_46_23_Pro.jpg"
]

image_size = (1080, 1080)
images = [Image.open(path).resize(image_size) for path in image_paths]
photo_images = [ImageTk.PhotoImage(image) for image in images]

# 2. Create an iterator to cycle through images forever
image_cycle = cycle(photo_images)

label = tk.Label(root)
label.pack()

def start_slideshow():
    # Get the next image from the cycle
    img = next(image_cycle)
    label.config(image=img)
    # Keep a reference so the image isn't garbage collected
    label.image = img 
    
    # 3. Schedule the NEXT update in 3000ms (3 seconds)
    root.after(3000, start_slideshow)

# Play button starts the cycle
play_button = tk.Button(root, text='Play Slide Show', command=start_slideshow)
play_button.pack()

root.mainloop()