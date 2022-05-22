# import tkinter as tk
# import time
# from math import cos
#
# SIZE = 150
#
# def meditate(root):
#     meditator = tk.Canvas(root, width=SIZE, height=SIZE, bg="#0080ff", bd=0)
#     meditator.grid(row=3, column=20)
#     circle = meditator.create_oval(0, 0, SIZE, SIZE, fill="white")
#     tm = 0
#     while tm < 5:
#         time.sleep(0.05)
#         tm += 0.05
#         root.update()
#         meditator.coords(circle, SIZE*(.2+.2*cos(tm)), SIZE*(.2+.2*cos(tm)), SIZE*(.8-.2*cos(tm)), SIZE*(.8-.2*cos(tm)))