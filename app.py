import tkinter as tk
import hashlib
import re
import sys
import subprocess
import random
# import webview
import webbrowser
import pygame

import meditation
import actual_stuff as stf

APP_NAME = "Phokus"

messagedisplay, timedisplay, main_screen = "   "
ws = ""

def fail(e, p):
    ...


def show_frame(frame):
    frame.tkraise()


def mood_music():
    webbrowser.open("https://www.youtube.com/watch?v=1ZYbU82GVz4&ab_channel=SoothingRelaxation")


def validate_login():
    e = str(email.get())
    w = workspace.get()
    global ws, send, service, partners
    from mail import sendmail
    send, service = sendmail.main()
    if "@" in w:
        msg = send(e, "Phokus Workspace", e.split("@")[0] + " has invited you to a new workspace.", w)

        ws = msg["id"]
        send(e, "Phokus Workspace", "Use the code " + ws + " to join.", w, ws)
        partners = w
    else:
        ws = w
        th = service.users().threads().get(userId="me", id=ws).execute()["messages"][-1]
        partners = sendmail.get_field(th, "to") + "," + sendmail.get_field(th, "from")
    main_screen_window()


def open_meditation():
    # window = webview.create_window("Meditate",
    #                                "https://lexhack-2022-meditate-website.github.io/LexHack-2022-Meditate-Website/",
    #                                width=800, height=600)
    # webview.start()
    webbrowser.open('https://lexhack-2022-meditate-website.github.io/LexHack-2022-Meditate-Website/')
    meditation.meditate(root)


# def open_buddy(email):
#     root.wm_withdraw()

def background_music():
    music = ["forest-lullaby-110624.mp3", "both-of-us-14037.mp3"]
    pygame.mixer.init()
    pygame.mixer.music.load(random.choice(music))
    pygame.mixer.music.play(loops=0)


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
        main_screen, text="Mood Music", width=20, height=10, command=background_music)
    music_button.grid(row=3, column=10)

    meditation_button = tk.Button(
        main_screen, text="Meditation", width=20, height=10, command=open_meditation)
    # meditation_button = tk.Button(
    #         main_screen, text="Meditation", width=20, height=10)
    meditation_button.grid(row=3, column=20)

    main_screen.update()
    stf.mainwindow(main_screen.update, str(email.get()), main_screen, buddy_button, pomodoro_button, music_button,
                   meditation_button, prnt, showtimer, ws, partners)


def main():
    global root, messagedisplay, timedisplay
    root = tk.Tk()
    root.title(f'{APP_NAME}--Login')
    root.geometry('350x200')
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
    # Get workspace
    tk.Label(root, text="Workspace").grid(row=3, column=0)
    global workspace
    workspace = tk.StringVar()
    tk.Entry(root, textvariable=workspace).grid(row=3, column=1)
    tk.Button(root, text="Login", command=validate_login).grid(row=4, column=0)
    tk.Label(root, text="To create a new workspace, enter a list of comma-separated emails", font=("TkDefaultFont", 7)).grid(row=5,columnspan=2)
    tk.Label(root, text="Alternatively, enter a workspace ID sent to you by a fellow Phokus user", font=("TkDefaultFont", 7)).grid(row=6, columnspan=2)
    root.mainloop()


def prnt(text):
    messagedisplay.config(text=text)
    main_screen.update()
    print(text)


def showtimer(text):
    timedisplay.config(text=text)
    main_screen.update()
    # print(text)
