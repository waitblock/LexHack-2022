import smtplib
import ssl

port = 465 
context = ssl.create_default_context()

login_details = open('credentials.login', 'r')
users = open('users.txt', 'r')
users_emails = users.readlines()

for user in users_emails:
    user.replace('\n', '')

'''
login_lines = login_details.readlines()
ln = login_lines[0]
email_username, email_password = ln.split(" ")
email_password = email_password.replace("\n", "")
'''
def do(username, password):
    message = f"""\
    Subject: Procrastination Accountability Buddy
    
    {str(username).partition('@')[0]} is looking for an accountability buddy to do their homework with"""

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        try:
            server.login(username, password)

            for user in users:
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