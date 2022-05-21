import tkinter as tk

APP_NAME = "Phokus"


def validate_login():
    with open("credentials.login", "w") as credentials_file:
        credentials_file.write(email.get()+"\n"+password.get())
    main_screen_window()
    return


def main_screen_window():
    root.wm_withdraw()
    main_screen = tk.Tk()
    main_screen.title(APP_NAME)
    main_screen.geometry('800x600')
    main_screen.resizable(False, False)
    title = tk.Label(main_screen, text=APP_NAME)
    title.config(font=("TkDefaultFont", 40))
    title.grid(row=0, column=0)
    buddy_button = tk.Button(main_screen, text="Buddy Chat/Time Remaining", width=20, height=10)
    buddy_button.grid(row=1, column=10)
    pomodoro_button = tk.Button(main_screen, text="Pomodoro Timer", width=20, height=10)
    pomodoro_button.grid(row=1, column=20)
    music_button = tk.Button(main_screen, text="Mood Music", width=20, height=10)
    music_button.grid(row=2, column=10)
    meditation_button = tk.Button(main_screen, text="Meditation", width=20, height=10)
    meditation_button.grid(row=2, column=20)

    main_screen.mainloop()


def main():
    global root
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
