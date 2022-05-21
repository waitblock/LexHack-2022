import smtplib
import ssl

port = 465 
context = ssl.create_default_context()

login_details = open('credentials.login', 'r')
users = open('users.txt', 'r')
users_emails = users.readlines()

for user in users_emails:
    user.replace('\n', '')

login_lines = login_details.readlines()
email_username = login_lines[0]
email_password = login_lines[1]

message = f"""\
Subject: Procrastination Accountability Buddy

{email_username.partition('@')[0]} is looking for an accountability buddy to do their homework with"""

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    try:
        server.login(email_username, email_password)
        
        for user in users:
            server.sendmail(email_username, users_emails, message)
        print("Sent")
    except Exception as e:
        print(e)

def broadcast(thing):
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as serve:
        try:
            serve.login(email_username, email_password)

            for user in users:
                serve.sendmail(email_username, users_emails, thing)
            print("Sent")
        except Exception as e:
            print(e)