from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

import os
from dotenv import load_dotenv

load_dotenv()

# Database Configuration
DATABASE_URL = os.getenv("DATABASE_URL")
assert DATABASE_URL, "DATABASE_URL environment variable is not set"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# SMTP Server Configuration
SMTP_USER = os.getenv("SMTP_USER")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")
SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = int(os.getenv("SMTP_PORT", 587))
assert SMTP_USER, "SMTP_USER environment variable is not set"
assert SMTP_PASSWORD, "SMTP_PASSWORD environment variable is not set"
assert SMTP_SERVER, "SMTP_SERVER environment variable is not set"
assert SMTP_PORT, "SMTP_PORT environment variable is not set"

# Logging Configuration
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
DEFAULT_LOG_DIR = f"{ROOT_DIR}/logs"
LOG_DIR = os.getenv("LOG_DIR", DEFAULT_LOG_DIR)

if not os.path.isdir(LOG_DIR):
  os.makedirs(LOG_DIR)

def apply_log_config():
  import time, logging
  current_time = time.strftime("%d-%m-%Y_%H-%M-%S")
  logging.basicConfig(
    filename=f"{LOG_DIR}/email_sender_{current_time}.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
  )
