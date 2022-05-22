import tkinter as tk
import hashlib
import re
import sys
import subprocess
import webview

import meditation
import actual_stuff as stf

APP_NAME = "Phokus"

messagedisplay, timedisplay, main_screen = "   "
ws = ""
partners = ""


def fail(e, p):
    ...


def show_frame(frame):
    frame.tkraise()


def validate_login():
    e = str(email.get())

    w = workspace.get()
    #print("!"+w+"!")
    global ws, send, service, partners
    from mail import sendmail
    send, service = sendmail.main()
    if "@" in w:
        msg = send(e, "Phokus Workspace", e.split("@")[0]+" has invited you to a new workspace.", w)
        #print(msg)
        ws = msg["id"]
        #print(ws)
        send(e, "Phokus Workspace", "Use the code "+ws+" to join.", w, ws)
        partners = w
    else:
        ws = w
        th = service.users().threads().get(userId="me", id=ws).execute()["messages"][-1]
        #print(th)
        partners = sendmail.get_field(th, "to")+","+sendmail.get_field(th, "from")

    main_screen_window()
    return True


def open_meditation():
    wind = webview.create_window('Hello world', 'https://lexhack-2022-meditate-website.github.io/LexHack-2022-Meditate-Website/')
    webview.start()


# def open_buddy(email):
#     root.wm_withdraw()


def main_screen_window():
    global main_screen
    root.wm_withdraw()
    main_screen = tk.Tk()
    main_screen.title(APP_NAME)
    main_screen.geometry('800x600')
    main_screen.resizable(False, False)

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
        main_screen, text="Buddy Chat/\nTime Remaining", width=20, height=10)
    buddy_button.grid(row=2, column=10)

    pomodoro_button = tk.Button(
        main_screen, text="Pomodoro Timer", width=20, height=10)
    pomodoro_button.grid(row=2, column=20)

    music_button = tk.Button(
        main_screen, text="Mood Music", width=20, height=10)
    music_button.grid(row=3, column=10)

    # meditation_button = tk.Button(
    #     main_screen, text="Meditation", width=20, height=10, command=open_meditation)
    meditation_button = tk.Button(
            main_screen, text="Meditation", width=20, height=10)
    meditation_button.grid(row=3, column=20)

    main_screen.update()
    stf.mainwindow(main_screen.update, str(email.get()), str(password.get()), main_screen, buddy_button, pomodoro_button, music_button,
                   meditation_button, prnt, showtimer, ws, partners)
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
    # Get workspace
    tk.Label(root, text="Workspace").grid(row=3, column=0)
    global workspace
    workspace = tk.StringVar()
    tk.Entry(root, textvariable=workspace).grid(row=3, column=1)
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
