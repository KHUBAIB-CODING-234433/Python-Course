import tkinter as tk
from itertools import cycle
from PIL import Image ,ImageTk
import time
root =tk.Tk()
root.title("image shower")
image_path  =[
    r"c:\Users\BUZZ TECH\OneDrive\Pictures\Camera Roll\khubauib.jpg",
    r"c:\Users\BUZZ TECH\OneDrive\Pictures\Camera Roll\student back .jpg",
    r"c:\Users\BUZZ TECH\OneDrive\Pictures\Camera Roll\WIN_20260225_09_46_23_Pro.jpg"

]

image_size =(1080,1080)
images = [Image.open(path).resize(image_size)for path in image_path]
photo_images =[ImageTk.PhotoImage(image)for image in images]

label =tk.Label(root)
label.pack()

def update_img():
    for images in photo_images:
        label.config(image=photo_images)
        label.update()
        label.sleep(3)

slide_show = cycle(photo_images)

def slide_show():
    for _ in range(len(image_path)):
        update_img()

play_button = tk.Button(root,text='play slide show',command=slide_show)
play_button.pack()
root.mainloop()
