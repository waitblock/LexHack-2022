import goals, meditation
from mail import chat_client

def mainwindow(update, email, main_screen, buddy_button, pomodoro_button, music_button, meditation_button, prnt, showtimer, workspace, partners):
    #sendmail = communication.do(email, password)
    pomodoro_button.bind("<ButtonRelease>", lambda x: goals.pomodoro(o1=prnt, o2=showtimer))
    # meditation_button.bind("<ButtonRelease>", lambda x: meditation.meditate(main_screen))
    buddy_button.bind("<ButtonRelease>", chat_client.chat_client(email, workspace, partners, main_screen))
    main_screen.mainloop()
