import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

app = tk.Tk()
app.title('test')
goals_display = tk.Text(app, height=12)

def select_goal_file():
    filetypes = (
        ('Text Files', '*.txt'),
        ('All files', '*.*')
    )

    goal_file = fd.askopenfile(
        title='Select a file',
        filetypes=filetypes)

    goals_display.insert('1.0', goal_file.readlines())


open_button = ttk.Button(
    app,
    text='Open a File',
    command=select_goal_file
)

open_button.pack(expand=True)

app.mainloop()