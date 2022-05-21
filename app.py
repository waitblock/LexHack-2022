import tkinter as tk


def validateLogin():
    with open("credentials.login", "w") as credentials_file:
        credentials_file.write(email.get()+"\n"+password.get())
    goToMainScreen()
    return


def goToMainScreen():
    main_screen = tk.Toplevel(root)
    root.wm_withdraw()
    main_screen.title('Phokus')
    main_screen.geometry('800x600')
    main_screen.resizeable(False, False)

    main_screen.mainloop()


def main():
    global root
    root = tk.Tk()
    root.title('Phokus--Login')
    root.geometry('300x200')
    root.resizable(False, False)
    
    # Title
    title = tk.Label(root, text="Login")
    title.config(font=('Helvetica bold', 30))
    title.grid(row=0, column=0)
    
    # Get email
    emailLabel = tk.Label(root, text="Email").grid(row=1, column=0)
    global email
    email = tk.StringVar()
    emailEntry = tk.Entry(root, textvariable=email).grid(row=1, column=1)
    
    # Get password
    passwordLabel = tk.Label(root, text="Password").grid(row=2, column=0)
    global password
    password = tk.StringVar()
    passwordEntry = tk.Entry(root, textvariable=password,
                             show="*").grid(row=2, column=1)
    loginButton = tk.Button(
        root, text="Login", command=validateLogin).grid(row=4, column=0)

    root.mainloop()
