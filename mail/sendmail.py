from mail import auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import base64
from email.mime.text import MIMEText

def main():
    creds = auth.authorize()
    service = build('gmail', 'v1', credentials=creds)

    def send(user, subject, content, targets, thread=None):
        if isinstance(targets, str):
            targets = [targets]
        message = MIMEText(content)
        message['To'] = ",".join(targets)
        message['From'] = user
        message['Subject'] = subject
        # encoded message
        encoded_message = base64.urlsafe_b64encode(message.as_bytes()) \
            .decode()
        message = {
            "raw": str(base64.urlsafe_b64encode(bytes(content, encoding="utf-8")), encoding="utf-8"),
            "payload": {
                  "headers": [
                        {"name": "To", "value": ",".join(targets)},
                        {"name": "From", "value": user},
                        {"name": "Subject", "value": subject}
                  ]
            },
        }
        if thread is not None:
            message["threadId"] = thread
        body = {"raw": encoded_message, "message": message}
        return service.users().messages().send(userId="me", body=body).execute()
    return send, service

if __name__ == "__main__":
    send, service = main()
    print(send("ez1liang@gmail.com", "test", "test", ["ez1liang@gmail.com", "decordofgammazeroplusone@gmail.com"]))
