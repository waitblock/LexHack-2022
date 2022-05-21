import app
import time

from app import prnt


def main():
    app.main()


if __name__ == "__main__":
    main()

with open('goals.txt', 'r+') as goal_file:
    goals = goal_file.readlines()
    goal_names = [line.partition('[')[0].replace('\n', '') for line in goals]
    goal_times = [line.partition('[')[2].replace(']', '').replace('\n', '') for line in goals]

    if goal_names[-1] == ' ':
        goal_names.pop()
    
    print(goal_times)
    print(goal_names)

def pomodoro(goal_times, goal_names):
    current_goal_time = goal_times[0]
    prnt("Please get rid of any distractions")
    timer = 5*60
    while timer > 0:
            m = timer // 60
            s = timer % 60
            print('{:02d}:{:02d}'.format(m, s))
            time.sleep(1)
            timer -= 1
    
    prnt("Begin your work")
    for i in range(current_goal_time // 25):
        timer = 25*60
        while timer > 0:
            m = timer // 60
            s = timer % 60
            print('{:02d}:{:02d}'.format(m, s))
            time.sleep(1)
            timer -= 1
        prnt("Time to take a break")

        timer = 5*60
        while timer > 0:
            m = timer // 60
            s = timer % 60
            print('{:02d}:{:02d}'.format(m, s))
            time.sleep(1)
            timer -= 1
        print("Get back to work")

    prnt("Time to review your work")
    timer = 5*60
    while timer > 0:
            m = timer // 60
            s = timer % 60
            print('{:02d}:{:02d}'.format(m, s))
            time.sleep(1)
            timer -= 1

    goal_times.remove(0)

def email_setup():
    print("placeholder")
