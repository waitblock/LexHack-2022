from googleapiclient.discovery import build
import tkinter as tk
from mail import sendmail
import base64
import time

def chat_client(email, workspace, members, root):
    window = tk.Toplevel(root)
    send, service = sendmail.main()
    chat = tk.Frame(window)
    chat.pack()
    def refresh():
        messages = service.users().threads().get(userId="me", id=workspace).execute()["messages"]
        for i in messages:
            if "UNREAD" in i["labelIds"]:
                service.users().messages().modify(userId='me', id=i["id"],
                                                  body={'removeLabelIds': ['UNREAD']}).execute()
                author = "Unknown"
                if sendmail.get_field(i, "from") is not None:
                    author = sendmail.get_field(i, "from")
                if author != email:
                    widget = tk.Label(chat,
                                      text=author + ": " + str(base64.urlsafe_b64decode(i["payload"]["body"]["data"]),
                                                               encoding="utf-8"))
                    widget.pack()
    def send_message(message):
        send(email, "Phokus", message, members, thread=workspace)
        widget = tk.Label(chat, text="Me: "+message, bg="#9ee3ff")
        widget.pack()
    bar = tk.Entry(window)
    button = tk.Button(window, text="Send")
    bar.pack()
    button.pack()
    button.bind("<ButtonRelease>", lambda x:send_message(bar.get()))
    messages = service.users().threads().get(userId="me", id=workspace).execute()["messages"]
    for i in messages:
        # print(i)
        service.users().messages().modify(userId='me', id=i["id"], body={'removeLabelIds': ['UNREAD']}).execute()
        author = "Unknown"
        if sendmail.get_field(i, "from") is not None:
            author = sendmail.get_field(i, "from")
        if author != email:
            widget = tk.Label(chat, text=author+": "+str(base64.urlsafe_b64decode(i["payload"]["body"]["data"]), encoding="utf-8"))
        else:
            widget = tk.Label(chat, text="Me: " + str(base64.urlsafe_b64decode(i["payload"]["body"]["data"]),
                                                             encoding="utf-8"), bg="#9ee3ff")
        widget.pack()
    while True:
        time.sleep(0.05)
        refresh()
        window.update()

if __name__ == "__main__":
    chat_client("ez1liang@gmail.com", "180ec864124d684b", ["ez1liang@gmail.com", "decordofgammazeroplusone@gmail.com"], tk.Tk())

