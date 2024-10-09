# Mailo - Mass Mailing Helper

Automatic Mail system with PostgreSQL database in the backend, integrated with SQLAlchemy ORM and Alemic migrations.

## License

This project is licensed under the GNU GPL-3.0 license.

## Setup

The project is written in Python 3.12.6, although should work on any Python Interpreter above 3.5.x.

For easy setup, create a python virtual environment and run:
    
```bash
pip install -r requirements.txt
# or
make init
```

Create a postgresql database, create a `.env` file in the root directory and add update it.

Make sure PostgreSQL is running, then run the following command for migrations in the root directory:

```bash
alemic upgrade head
```

## Usage

There is no framework used, so there is only scripts for specific tasks.

`src/storage.py` is used to update the database with a tabular data like an excel sheet, by entering the path to the file, column for the names and emails, plus the event code.

`src/sender.py` is used to send emails to a list of recipients. There is no specific automation in that script for now, everything is entered manually to the script according to the needs.

Every time `sender.py` is run, it creates a log file with the email details and the status of the email sent to the recipients.


## Details for ITU AI Usage

Event codes in the databases are used to identify the events participants are registered to.

Following event codes are used in the databases:
- `datathonai22`
- `aisummit22`
- `aisummit23`
- `aisummit24`
