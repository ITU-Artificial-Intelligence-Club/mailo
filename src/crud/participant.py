from sqlalchemy.orm import Session
from entities.participant import Participant

def register_participant(db: Session, name: str, email: str, events_attended: str) -> Participant:
  new_participant = Participant(
    name=name,
    email=email,
    events_attended=events_attended
  )
  db.add(new_participant)
  db.commit()
  return new_participant

def update_participant(db: Session, participant: Participant, name: str, email: str, events_attended: str) -> Participant:
  participant.name = name
  participant.email = email
  participant.events_attended = events_attended
  db.commit()
  return participant

def get_all_participants(db: Session) -> list[Participant]:
  return db.query(Participant).all()

def get_participant_by_id(db: Session, id: int) -> Participant | None:
  return db.query(Participant).filter(Participant.id == id).first()

def get_participant_by_email(db: Session, email: str) -> Participant | None:
  return db.query(Participant).filter(Participant.email == email).first()

def delete_participant_by_id(db: Session, id: int) -> bool:
  participant = db.query(Participant).filter(Participant.id == id).first()
  if not participant:
    return False
  db.delete(participant)
  db.commit()
  return True
