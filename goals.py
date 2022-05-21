with open('goals.txt', 'r+') as goal_file:
    goals = goal_file.readlines()
    goal_names = [line.partition('[')[0].replace('\n', '') for line in goals]
    goal_times = [line.partition('[')[2].replace(']', '').replace('\n', '') for line in goals]

    if goal_names[-1] == ' ':
        goal_names.pop()

    print(goal_times)
    print(goal_names)

def pomodoro(goal_times):
    current_goal_time = goal_times[0]

def email_setup():
    print("placeholder")