import smtplib
import ssl

port = 465 
context = ssl.create_default_context()

login_details = open('credentials.login', 'r')
email_username = login_details.readlines()[0]
email_password = login_details.readlines()[1]

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login(email_username, email_password)
    server.sendmail(email_username, 'ez26301300@gmail.com', 'test')
    