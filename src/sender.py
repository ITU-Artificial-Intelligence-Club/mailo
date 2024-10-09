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
  body = "This is a test email sent from Python!"

  to_emails = ["ertugrul.a.senturk@gmail.com"] * 10
  
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
