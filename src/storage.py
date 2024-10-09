from services.storage import import_participant

if __name__ == "__main__":
  import argparse
  parser = argparse.ArgumentParser()
  parser.add_argument("file_path", help="The path of the file to import")
  parser.add_argument("name_column", help="The column containing the name")
  parser.add_argument("email_column", help="The column containing the emails")
  parser.add_argument("event_code", help="Code of the event to be added in the 'events_attende' field in the database")
  args = parser.parse_args()
  file_path = args.file_path
  name_column = args.name_column
  email_column = args.email_column
  event_code = args.event_code
  import_participant(file_path, name_column, email_column, event_code)
