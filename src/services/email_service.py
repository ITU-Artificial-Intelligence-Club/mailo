import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import logging

def send_emails(smtp_server: str, smtp_port: int, username: str, password: str, to_emails: list[str], subject: str, body):
  try:
    # Set up the server
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(username, password)
    logging.info(f"Logged in to the SMTP server at {smtp_server}:{smtp_port} as {username}")
    for to_email in to_emails:
      # Create a multipart message
      msg = MIMEMultipart()
      msg['From'] = username
      msg['To'] = to_email
      msg['Subject'] = subject

      # Attach the email body
      msg.attach(MIMEText(body, 'html'))

      try:
        server.send_message(msg)
        print(f"Email sent to {to_email}")
        logging.info(f"Email sent to {to_email}")
      except Exception as e:
        print(f"Failed to send email to {to_email}: {str(e)}")
        logging.error(f"Failed to send email to {to_email}: {str(e)}")
  except Exception as e:
    print(f"Failed to connect to the SMTP server at {smtp_server}:{smtp_port}: {str(e)}")
    logging.error(f"Failed to connect to the SMTP server at {smtp_server}:{smtp_port}: {str(e)}")
  finally:
    server.quit()
