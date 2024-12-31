# Annual Holiday Planner
This is just a Python script to create an A4 PDF for our annual holiday planning.

The calendar incorporates:

* WA and ACT's public holidays (automated)
* School Holidays (manual config)
* Birthdays (of your choosing)

# Setup instructions
Requirements: Python 3.x

Install the dependencies for Public Holidays and PDF creation:

```
python -m venv venv
. venv/bin/activate
pip install -r requirements.txt
```

# Creating a calendar

* Change the `YEAR` in `config.py`
* Update the [WA](https://www.wa.gov.au/service/employment/workplace-arrangements/public-holidays-western-australia) and [ACT](https://www.act.gov.au/living-in-the-act/public-holidays-school-terms-and-daylight-savings) school holidays for your desired year in `config.py`
* Create `birthdays.py` from `birthdays.tmpl.py` and configure any birthdays you wish to include

With all that said and done, now just run:

```
python generate.py
````

And hey presto, `planner.pdf` should appear! 🎉