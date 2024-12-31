import datetime

YEAR = 2025

SCHOOL_HOLIDAYS = [
  {
    "name": "Term 1",
    "start_date": datetime.date(YEAR, 4, 12),
    "end_date": datetime.date(YEAR, 4, 27)
  },
  {
    "name": "Term 2",
    "start_date": datetime.date(YEAR, 7, 5),
    "end_date": datetime.date(YEAR, 7, 20)
  },
  {
    "name": "Term 3",
    "start_date": datetime.date(YEAR, 9, 27),
    "end_date": datetime.date(YEAR, 10, 12)
  },
  {
    "name": "Term 4",
    "start_date": datetime.date(YEAR, 12, 18),
    "end_date": datetime.date(YEAR + 1, 2, 1)
  }
]