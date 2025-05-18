import os

import yagmail
from content import create_file_with_content
from dotenv import load_dotenv

EMAIL_USER = os.environ['EMAIL_USER']
EMAIL_PASSWORD = os.environ['GMAIL_APP_PASSWORD']
FILE_NAME = 'daily_news.txt'

load_dotenv()
create_file_with_content()


def send_email():
	try:
		with open(FILE_NAME) as f:
			message = f.read()
	except OSError as e:
		print(f'Unable to open file: {FILE_NAME}.\nError: {e}')

	email = yagmail.SMTP(user=EMAIL_USER, password=EMAIL_PASSWORD)
	email.send(to='wakula993@gmail.com', subject='Test mail', contents=message)  # type: ignore


if __name__ == '__main__':
	send_email()
