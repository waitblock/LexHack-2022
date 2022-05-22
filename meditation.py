import tkinter as tk
import time
from math import cos

XSIZE = 800
YSIZE = 600

def meditate(root):
    meditator = tk.Canvas(root, width=XSIZE, height=YSIZE, bg="#0080ff")
    meditator.place(x=0,y=0)
    circle = meditator.create_oval(0, 0, YSIZE, YSIZE, fill="white")
    tm = 0
    while tm < 2*60:
        time.sleep(0.05)
        tm += 0.05
        root.update()
        meditator.coords(circle, 100+YSIZE*(.2+.1*cos(tm)), YSIZE*(.2+.1*cos(tm)), 100+YSIZE*(.8-.1*cos(tm)), YSIZE*(.8-.1*cos(tm)))
    meditator.destroy()
