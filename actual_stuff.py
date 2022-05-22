import communication, goals, meditation

def mainwindow(update, email, password, main_screen, buddy_button, pomodoro_button, music_button, meditation_button, prnt, showtimer):
    #sendmail = communication.do(email, password)
    pomodoro_button.bind("<ButtonRelease>", lambda x: goals.pomodoro(o1=prnt, o2=showtimer))
    meditation_button.bind("<ButtonRelease>", lambda x: meditation.meditate(main_screen))
    main_screen.mainloop()