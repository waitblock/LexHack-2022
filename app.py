import tkinter as tk
import hashlib
import re
import sys
import subprocess

import actual_stuff as stf

APP_NAME = "Phokus"

messagedisplay, timedisplay, main_screen = "   "


def fail(e, p):
    ...


def show_frame(frame):
    frame.tkraise()


def validate_login():
    e = str(email.get())
    p = str(password.get())
    pdigest = hashlib.sha512(bytes(p, encoding="utf-8")).hexdigest()
    if not re.match(r"^\S{1,}@\S{2,}\.\S{2,}$", e):
        fail(e, p)
        return False
    f = open("users.txt")
    if e + "\n" in f.readlines():  # known user
        g = open("credentials.login")
        for i in g.readlines():
            if i.startswith(e + " "):
                if i == e + " " + pdigest + "\n":
                    main_screen_window()
                    return True
                fail(e, p)
                return False
        g.close()
    f.close()
    with open("credentials.login", "w") as credentials_file:
        credentials_file.write(e+" "+pdigest+"\n")

    with open("users.txt", "w") as users:
        users.write(e + "\n")

    main_screen_window()
    return True


def open_meditation():
    if sys.platform == "win32":
        subprocess.call(["start", "meditate.exe"])
    if sys.platform == "darwin":
        subprocess.call(["/usr/bin/open", "-W", "-n", "-a",
                         "meditate.app"])


# def open_buddy(email):
#     root.wm_withdraw()


def main_screen_window():
    global main_screen
    root.wm_withdraw()
    main_screen = tk.Tk()
    main_screen.title(APP_NAME)
    main_screen.geometry('800x600')
    main_screen.resizable(False, False)

    buddy_frame = tk.Frame(root)
    pomodoro_frame = tk.Frame(root)
    music_frame = tk.Frame(root)

    global messagedisplay, timedisplay
    nwindow = tk.Frame(main_screen)
    # message display
    messagedisplay = tk.Label(nwindow, text="")
    messagedisplay.grid(row=0, column=0)  # help
    # time display
    timedisplay = tk.Label(nwindow, text="")
    timedisplay.grid(row=0, column=1)  # help

    nwindow.grid(row=0, columnspan=2)

    title = tk.Label(main_screen, text=APP_NAME)
    title.config(font=("TkDefaultFont", 40))
    title.grid(row=1, column=0)

    buddy_button = tk.Button(
        main_screen, text="Buddy Chat/\nTime Remaining", width=20, height=10, command=lambda:show_frame(buddy_frame))
    buddy_button.grid(row=2, column=10)

    pomodoro_button = tk.Button(
        main_screen, text="Pomodoro Timer", width=20, height=10)
    pomodoro_button.grid(row=2, column=20)

    music_button = tk.Button(
        main_screen, text="Mood Music", width=20, height=10, command=lambda:show_frame(music_frame))
    music_button.grid(row=3, column=10)

    meditation_button = tk.Button(
        main_screen, text="Meditation", width=20, height=10, command=open_meditation)
    meditation_button.grid(row=3, column=20)

    main_screen.update()
    stf.mainwindow(main_screen.update, str(email.get()), str(password.get()), main_screen, buddy_button, pomodoro_button, music_button,
                   meditation_button, prnt, showtimer)
    main_screen.after(1, lambda: stf.mainwindow(str(email.get()), str(password.get(
    )), main_screen, buddy_button, pomodoro_button, music_button, meditation_button, prnt, showtimer))
    main_screen.mainloop()


def main():
    global root, messagedisplay, timedisplay
    root = tk.Tk()
    root.title(f'{APP_NAME}--Login')
    root.geometry('300x200')
    root.resizable(False, False)
    # Title
    title = tk.Label(root, text="Login")
    title.config(font=("TkDefaultFont", 30))
    title.grid(row=0, column=0)
    # Get email
    tk.Label(root, text="Email").grid(row=1, column=0)
    global email
    email = tk.StringVar()
    tk.Entry(root, textvariable=email).grid(row=1, column=1)
    # Get password
    tk.Label(root, text="Password").grid(row=2, column=0)
    global password
    password = tk.StringVar()
    tk.Entry(root, textvariable=password, show="*").grid(row=2, column=1)
    tk.Button(root, text="Login", command=validate_login).grid(row=4, column=0)

    root.mainloop()


def prnt(text):
    messagedisplay.config(text=text)
    main_screen.update()
    print(text)


def showtimer(text):
    timedisplay.config(text=text)
    main_screen.update()
    # print(text)
