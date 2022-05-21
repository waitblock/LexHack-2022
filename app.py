import tkinter as tk
import hashlib, re

APP_NAME = "Phokus"

messagedisplay, timedisplay = "Yes", "Yes"


def fail(e, p):
    ...


def validate_login():
    e = email.get()
    p = password.get()
    pdigest = hashlib.sha512(bytes(p,encoding="utf-8")).hexdigest()
    if not re.match(r"^\S{1,}@\S{2,}\.\S{2,}$", e):
        fail("e, p")
        return False
    f = open("users.txt")
    if e + "\n" in f.readlines(): # known user
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


def main_screen_window():
    root.wm_withdraw()
    main_screen = tk.Tk()
    main_screen.title(APP_NAME)
    main_screen.geometry('800x600')
    main_screen.resizable(False, False)

    title = tk.Label(main_screen, text=APP_NAME)
    title.config(font=("TkDefaultFont", 40))
    title.grid(row=0, column=0)

    buddy_button = tk.Button(main_screen, text="Buddy Chat/\nTime Remaining", width=20, height=10)
    buddy_button.grid(row=1, column=10)

    pomodoro_button = tk.Button(main_screen, text="Pomodoro Timer", width=20, height=10)
    pomodoro_button.grid(row=1, column=20)

    music_button = tk.Button(main_screen, text="Mood Music", width=20, height=10)
    music_button.grid(row=2, column=10)

    meditation_button = tk.Button(main_screen, text="Meditation", width=20, height=10)
    meditation_button.grid(row=2, column=20)

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
    # message display
    messagedisplay = tk.Label(root, text="")
    messagedisplay.grid(row=1, column=0)#help
    # time display
    timedisplay = tk.Label(root, text="")
    timedisplay.grid(row=2, column=0)#help
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
    messagedisplay.update(text=text)
    print(text)

    
def showtimer(text):
    timedisplay.update(text=text)
    #print(text)
