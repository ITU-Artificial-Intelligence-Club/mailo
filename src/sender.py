import logging

from config import (
  SMTP_SERVER,
  SMTP_PORT,
  SMTP_USER,
  SMTP_PASSWORD,
  apply_log_config
)
from services.email_service import send_emails

if __name__ == "__main__":
  subject = "Test Email"
  to_emails = ["ertugrul.a.senturk@gmail.com"] * 10
  try:
    with open("mail_template.html") as body_file:
      body = body_file.read()
  except Exception as e:
    print("Could not open mail body file: ", e)
    exit(1)
  
  apply_log_config()

  logging.info(f"Sending emails to {len(to_emails)} recipients with subject of '{subject}'\n\nEmail body is:\n\n{body}\n\n")

  send_emails(
    SMTP_SERVER,
    SMTP_PORT,
    SMTP_USER,
    SMTP_PASSWORD,
    to_emails,
    subject,
    body
  )
