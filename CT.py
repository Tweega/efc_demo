import os
import tkinter as tk
from PIL import Image, ImageTk

#image_list = ['img_1.jpg', 'img_2.jpg', 'img_3.jpg', 'img_4.jpg', 'img_5.jpg']
current = 0


image_list = [x for x in os.listdir() if x.upper().endswith(".JPG")]
#print(image_list)


def move(delta):
    global current, image_list

    current += delta
    current = current % len(image_list)
    image = Image.open(image_list[current])
    out = image.resize( [800, 480] )
    photo = ImageTk.PhotoImage(out)
    #label['text'] = text_list[current]
    label['image'] = photo
    label.anyAttributeMountsImage = photo


def keyup(key):
    n = int(key.char)
    if n == 0:
        exit()

    x = 0
    if n > current:
        x = n - current - 1
    else:
        x = (len(image_list) - current) + n - 1
    move(x)

def doLeftClick(m):
    move(1)

def doRightClick(m):
    move(-1)

root = tk.Tk()

label = tk.Label(root, compound=tk.TOP)
label.bind("<Button-1>", doLeftClick)
label.bind("<Button-3>", doRightClick)
label.bind("<Double-Button-3>", lambda z: exit())
label.pack()

frame = tk.Frame(root)
frame.bind("<KeyRelease>", keyup)
frame.focus_set()

frame.pack()

move(0)
root.overrideredirect(1)
root.mainloop()
