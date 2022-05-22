from mail import auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import base64
from email.mime.text import MIMEText

def get_field(email, field_name):
    header = email['payload']['headers']
    for m in header:
        if m['name'] == field_name:
            return m['value']

def main():
    creds = auth.authorize()
    service = build('gmail', 'v1', credentials=creds)

    def send(user, subject, content, targets, thread=None):
        if isinstance(targets, str):
            targets = [targets]
        '''
        message = MIMEText(content)
        message['To'] = ",".join(targets)
        message['From'] = user
        message['Subject'] = subject
        if thread is not None:
            message["threadId"] = thread
        # encoded message
        encoded_message = base64.urlsafe_b64encode(message.as_bytes()) \
            .decode()
        message = {
            "raw": str(base64.urlsafe_b64encode(bytes(content, encoding="utf-8")), encoding="utf-8"),
            "payload": {
                "headers": [
                    {"name": "To", "value": ",".join(targets)},
                    {"name": "From", "value": user},
                    {"name": "Subject", "value": subject},
                ]
            },
        }
        if thread is not None:
            message["threadId"] = thread
            ids = []
            th = service.users().threads().get(userId="me", id=thread).execute()
            for i in th["messages"]:
                print(i)
                ids.append(get_field(i, "Message-Id"))
            message["payload"]["headers"].append({"name": "In-Reply-To", "value": ids[0]})
            message["payload"]["headers"].append({"name": "References", "value": ",".join(ids)})
        body = {"raw": encoded_message, "message": message}
        return service.users().messages().send(userId="me", body=body).execute()
        '''
        message = MIMEText(content)
        message['from'] = user
        message['to'] = ",".join(targets)
        message['subject'] = subject
        if thread is not None:
            ldate = 0
            last = ""
            th = service.users().threads().get(userId="me", id=thread).execute()
            for i in th["messages"]:
                #print(i)
                if int(i["internalDate"]) > ldate:
                    last = i
            message['In-Reply-To'] = get_field(last, "Message-Id")
            try:
                message['References'] = get_field(last, "Message-Id") + " " + get_field(last, "References")
            except:
                message['References'] = get_field(last, "Message-Id")

        return service.users().messages().send(userId="me", body={
            'raw': base64.urlsafe_b64encode(message.as_string().encode()).decode(),
            'threadId': thread
        }).execute()
    return send, service

if __name__ == "__main__":
    send, service = main()
    print(send("ez1liang@gmail.com", "test", "test", ["decordofgammazeroplusone@gmail.com"], '180ecd5d2b88d9b0'))
