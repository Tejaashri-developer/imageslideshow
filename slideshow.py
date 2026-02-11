from itertools import cycle
from PIL import Image, ImageTk
import time
import tkinter as tk


#creating a root file where the image is displayed with the titile
root=tk.Tk()
root.title("Image slideshow viewer")

#list of image path
Image_paths = [
    r"/Users/tejaashrigovulakkapu/Python projects/images for slide show/IMG_0347.JPG",
    r"/Users/tejaashrigovulakkapu/Python projects/images for slide show/IMG_2689 (1).png",
    r"/Users/tejaashrigovulakkapu/Python projects/images for slide show/Profile_picture__1 (1).png",
]

#resizing the images to 1080*1080
image_size=(1080,1080)
images=[Image.open(path).resize(image_size) for path in Image_paths]
photo_images=[ImageTk.PhotoImage(image) for image in images]

label = tk.Label(root)
label.pack()

def update_image():
    for photo_image in photo_images:
        label.config(image=photo_image)
        label.update()
        time.sleep(3)

slideshow = cycle(photo_images)

def start_slideshow():
    for _ in range (len(Image_paths)):
        update_image()

play_button = tk.Button(root, text='Play slideshow', command= start_slideshow)
play_button.pack()
 
root.mainloop()
