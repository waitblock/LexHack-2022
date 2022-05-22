import time
import math

with open('goals.txt', 'r+') as goal_file:
    goals = goal_file.readlines()
    goal_names = [line.partition('[')[0].replace('\n', '') for line in goals]
    goal_times = [int(line.partition('[')[2].replace(
        ']', '').replace('\n', '')) for line in goals]

    if goal_names[-1] == ' ':
        goal_names.pop()

    print(goal_times)
    print(goal_names)


def pomodoro(o1=print, o2=print):
    current_goal_time = goal_times[0]
    o1("Please get rid of any distractions")
    timer = current_goal_time / 7 * 60
    while timer > 0:
        m = timer // 60
        s = timer % 60
        o2('{:02d}:{:02d}'.format(m, s))
        time.sleep(1)
        timer -= 1

    o1("Begin your work")
    for i in range(current_goal_time // 25):
        timer = 25 * 60
        while timer > 0:
            m = timer // 60
            s = timer % 60
            o2('{:02d}:{:02d}'.format(m, s))
            time.sleep(1)
            timer -= 1
        o1("Time to take a break")
        timer = 5 * 60
        while timer > 0:
            m = timer // 60
            s = timer % 60
            o2('{:02d}:{:02d}'.format(m, s))
            time.sleep(1)
            timer -= 1
        o1("Get back to work")
    o1("Time to review your work")
    timer = current_goal_time / 7 * 60
    while timer > 0:
        m = timer // 60
        s = timer % 60
        o2('{:02d}:{:02d}'.format(m, s))
        time.sleep(1)
        timer -= 1
    goal_times.remove(0)
