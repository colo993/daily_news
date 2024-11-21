import os
import yagmail

from dotenv import load_dotenv
from content import create_file

load_dotenv()

create_file()
email_user = os.environ["EMAIL_USER"]
email_password = os.environ["GMAIL_APP_PASSWORD"]

def send_email():
    with open('daily_news.txt') as f:
        message = f.read()
    email = yagmail.SMTP(user=email_user, password=email_password)
    email.send(to="wakula993@gmail.com", subject="Test mail", contents=message)


if __name__ == "__main__":
    send_email()
