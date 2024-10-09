import pandas as pd
from db import SessionLocal
from crud import register_participant, update_participant, get_participant_by_email
from utils import AttendedEventUtils
from sqlalchemy.orm import Session


def excel_column_to_index(column_label: str):
    """
    Convert Excel column labels ('A', 'B', 'C', etc.) to zero-indexed column numbers.
    """
    column_label = column_label.upper()
    result = 0
    for i, char in enumerate(reversed(column_label)):
        result += (ord(char) - ord('A') + 1) * (26 ** i)
    return result - 1  # Zero-indexed


def register_or_update_participant(db: Session, name: str, email: str, event_code: str):
  """
  Register a new participant or update an existing participant with the given event code.
  """
  participant = get_participant_by_email(db, email)
  if participant:
    events_attended = participant.events_attended
    if not AttendedEventUtils.has_event_code(events_attended, event_code):
      events_attended = AttendedEventUtils.add_event_code(events_attended, event_code)
      update_participant(db, participant, name, email, events_attended)
  else:
    register_participant(db, name, email, event_code)


def import_participant(file_path: str, name_column: str, email_column: str, event_code: str):
  db = SessionLocal()
  df = pd.read_excel(file_path)
  i = 0
  name_column_index = excel_column_to_index(name_column)
  email_column_index = excel_column_to_index(email_column)
  if email_column_index < len(df.columns) and name_column_index < len(df.columns):
    emails = df.iloc[:, email_column_index]
    names = df.iloc[:, name_column_index]
    for name, email in zip(names, emails):
      if pd.isnull(name) or pd.isnull(email):
        continue
      register_or_update_participant(db, name, email, event_code)
      i += 1
  else:
    if name_column_index >= len(df.columns):
      print(f"Name column {name_column} does not exist.")
    if email_column_index >= len(df.columns):
      print(f"Email column {email_column} does not exist.")
  print(f"Total emails: {i}")
  db.close()
