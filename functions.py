from birthdays import BIRTHDAYS
from config import SCHOOL_HOLIDAYS


def get_birthday_name(date):
  for birthday in BIRTHDAYS:
    if date == birthday["date"]:
      return birthday["name"]
  return None

def is_date_a_birthday(date):
  for birthday in BIRTHDAYS:
    if date == birthday["date"]:
      return True
  return False

def is_school_holiday_start_date(date):
  for hol in SCHOOL_HOLIDAYS:
    if date == hol["start_date"]:
      return True
  return False

def is_school_holiday_end_date(date):
  for hol in SCHOOL_HOLIDAYS:
    if date == hol["end_date"]:
      return True
  return False