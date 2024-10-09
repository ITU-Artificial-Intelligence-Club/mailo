class AttendedEventUtils:
  @staticmethod
  def event_string_to_list(event_string: str) -> list[str]:
    """
    Convert a string of events separated by commas to a list of events.
    """
    return event_string.split(",")
  
  @staticmethod
  def event_list_to_string(event_list: list[str]) -> str:
    """
    Convert a list of events to a string of events separated by commas.
    """
    return ",".join(event_list)

  @staticmethod
  def has_event_code(events: str, event_code: str) -> bool:
    """
    Check if a list of events contains a specific event code.
    """
    return event_code in AttendedEventUtils.event_string_to_list(events)
  
  @staticmethod
  def add_event_code(events: str, event_code: str) -> str:
    """
    Add an event code to a list of events.
    """
    event_list = AttendedEventUtils.event_string_to_list(events)
    event_list.append(event_code)
    return AttendedEventUtils.event_list_to_string(event_list)
