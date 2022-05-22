import communication, goals, time

def mainwindow(update, email, password, main_screen, buddy_button, pomodoro_button, music_button, meditation_button, prnt, showtimer):
    #sendmail = communication.do(email, password)
    pomodoro_button.bind("<ButtonRelease>", lambda x: goals.pomodoro(["a", "b", "c", "d", "e", "f", "g"], o1=prnt, o2=showtimer))
    main_screen.mainloop()