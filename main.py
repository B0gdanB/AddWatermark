# Python program to create
# a file explorer in Tkinter

# import all components
# from the tkinter library
from tkinter import *

# import filedialog module
from tkinter import filedialog

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


# import matplotlib.pyplot as plt
# import numpy as np

# Function for opening the
# file explorer window
def browseFiles():
    filenames = filedialog.askopenfilenames(initialdir="/",
                                            title="Select a File",
                                            filetypes=(("Image files",
                                                        "*.jpg*"),
                                                       ("all files",
                                                        "*.*")))

    # Change label contents
    label_file_explorer.configure(text="Done! New files saved to the same directory.")

    # image opening
    for item in filenames:
        image = Image.open(item)
        # this open the photo viewer
        # image.show()
        # text Watermark
        watermark_image = image.copy()
        draw = ImageDraw.Draw(watermark_image)
        # ("font type",font size)
        w, h = image.size
        x, y = int(w / 2), int(h / 2)
        if x > y:
            font_size = y
        elif y > x:
            font_size = x
        else:
            font_size = x

        font = ImageFont.truetype("arial.ttf", int(font_size / 6))

        # add Watermark
        # (0,0,0)-black color text  (255,255,255)-White color text
        # draw.text((x, y), "My Web Site", fill=(255, 255, 255), font=font, anchor='ms')
        draw.text((x, y), f"{water_mark_entry.get()}", fill=(255, 255, 255), font=font, anchor='ms')
        # watermark_image.show()
        watermark_image.save(f"{item[:-4]}_watermark.jpg")


# Create the root window
window = Tk()

# Set window title
window.title('Add Water Mark')

# Set window size
window.geometry("500x300")

# Set window background color
window.config(background="white")

# Create a File Explorer label
label_file_explorer = Label(window,
                            text="Add Water Mark",
                            width=70, height=4,
                            fg="blue")

water_mark_entry = Entry(width=40)
water_mark_entry.grid(column=1, row=2, )
water_mark_entry.insert(0, "Type your watermark")

button_explore = Button(window,
                        text="Browse Images",
                        command=browseFiles)

button_exit = Button(window,
                     text="Exit",
                     command=exit)

# Grid method is chosen for placing
# the widgets at respective positions
# in a table like structure by
# specifying rows and columns
label_file_explorer.grid(column=1, row=1)

button_explore.grid(column=1, row=3)

button_exit.grid(column=1, row=4)

# Let the window wait for any events
window.mainloop()
