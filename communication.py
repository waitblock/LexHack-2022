import smtplib
import ssl
import pickle

with open('goals.txt', 'r+') as goal_file:
    goals = goal_file.readlines()
    goal_names = [line.partition('[')[0].replace('\n', '') for line in goals]
    goal_times = [line.partition('[')[2].replace(
        ']', '').replace('\n', '') for line in goals]

    for goal in goal_names:
        if goal[-1] == ' ':
            goal_names[goal_names.index(goal)] = goal[:-1]

    goal_names[-1] = 'and ' + goal_names[-1]
    goal_times[-1] = 'and ' + goal_times[-1]

port = 465
context = ssl.create_default_context()

login_details = open('credentials.login', 'r')
users = open('users.txt', 'r')
users_emails = users.readlines()

for user in users_emails:
    users_emails[users_emails.index(user)] = user.replace('\n', '')
    print(user)

login_lines = login_details.readlines()
email_username = login_lines[0]
email_password = login_lines[1]

message = f"""\
Subject: Procrastination Accountability Buddy

{email_username.partition('@')[0]} is looking for an accountability buddy to do their homework with. Their goals are {', '.join(goal_names)} and they want to spend {' minutes, '.join(goal_times)} minutes on those tasks respectively"""

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    try:
        server.login(email_username, email_password)
        print(users_emails)
        server.sendmail(email_username, users_emails, message)
        print("Sent")
    except Exception as e:
        print(e)
