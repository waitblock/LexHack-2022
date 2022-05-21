import communication, goals

def mainwindow(update, email, password, main_screen, buddy_button, pomodoro_button, music_button, meditation_button, prnt, showtimer):
    #sendmail = communication.do(email, password)
    goals.pomodoro(["a", "b", "c", "d", "e", "f", "g"], o1=prnt, o2=showtimer, update=update) #TODO:someone figure out why goals.pomodoro is crashing tkinter
    ...