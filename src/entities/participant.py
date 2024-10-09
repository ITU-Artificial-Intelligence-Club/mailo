from sqlalchemy import Column, Integer, String
from config import Base

class Participant(Base):
  __tablename__ = 'participants'

  id = Column(
    Integer,
    primary_key=True,
    index=True
  )

  name = Column(
    String,
    nullable=False
  )

  email = Column(
    String,
    unique=True,
    nullable=False
  )

  events_attended = Column(
    String,
    nullable=False,
    default=""
  )
