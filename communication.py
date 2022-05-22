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
ln = login_lines[0]
email_username, email_password = ln.split(" ")
email_password = email_password.replace("\n", "")


def do(username, password, goal_names, goal_times):
    message = f"""\
Subject: Procrastination Accountability Buddy

{username.partition('@')[0]} is looking for an accountability buddy to do their homework with. Their goals are {', '.join(goal_names)} and they want to spend {' minutes, '.join(goal_times)} minutes on those tasks respectively"""

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        try:
            server.login(username, password)
            server.sendmail(username, users_emails, message)
            print("Sent")
        except Exception as e:
            print(e)

    def broadcast(thing):
        with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as serve:
            try:
                serve.login(username, password)

                for user in users:
                    serve.sendmail(username, users_emails, thing)
                print("Sent")
            except Exception as e:
                print(e)
    return broadcast