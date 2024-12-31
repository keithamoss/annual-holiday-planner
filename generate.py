import calendar
import datetime

import holidays
import weasyprint

from config import YEAR
from functions import (get_birthday_name, is_date_a_birthday,
                       is_school_holiday_end_date,
                       is_school_holiday_start_date)

au_wa_holidays = holidays.AU(subdiv="WA", years=YEAR)
au_act_holidays = holidays.AU(subdiv="ACT", years=YEAR)

with open("planner.html", "w") as f:
  f.write('<link href="reset.css" rel="stylesheet" />')
  f.write('<link href="planner.css" rel="stylesheet" />')
  f.write('<link href="special_days.css" rel="stylesheet" />')

  f.write("<table border='1' width='100%' height='100%'>\n")

  f.write(f'<tr class="year"><th colspan="12">{YEAR}</th></tr>')

  f.write('<tr class="months">\n')
  for month_num in range(1, 13):
    f.write(f"<th>{datetime.date(YEAR, month_num, 1):%B}</th>\n")
  f.write("</tr>\n\n")

  for dayNum in range(1, 32):
    f.write("<tr>\n")

    for monthNum in range(1, 13):
      numDaysInMonth = calendar.monthrange(YEAR, monthNum)[1]

      if dayNum <= numDaysInMonth:
        date = datetime.date(YEAR, monthNum, dayNum)

        classNames = []
        cellText = [f'{dayNum}']

        dayName = f"{date:%A}"
        if dayName == "Saturday" or dayName == "Sunday":
          classNames.append("weekend")
        else:
          classNames.append("weekday")
        
        if is_date_a_birthday(date):
          classNames.append("birthday")
          cellText.append(f'{get_birthday_name(date)}\'s Bday')
        
        if date in au_wa_holidays:
          classNames.append("wa_pub_hol")
        
        if date in au_act_holidays:
          classNames.append("act_pub_hol")
        
        if is_school_holiday_start_date(date):
          classNames.append("school_hol_start")
        
        if is_school_holiday_end_date(date):
          classNames.append("school_hol_end")

        f.write(f'<td class="{(" ").join(classNames)}">{(" ").join(cellText)}</td>\n')
      else:
        f.write(f'<td class="empty"></td>\n')
    f.write("</tr>\n\n")

  # For debugging all possible combinations of special days
#   f.write("""
#     <tr>
#       <td class="weekday wa_pub_hol birthday">Wkday, WA PH, Bday</td>
#       <td class="weekday act_pub_hol birthday">Wkday, ACT PH, Bday</td>
          
#       <td class="weekday wa_pub_hol act_pub_hol">Wkday, WA PH, ACT</td>
#       <td class="weekday wa_pub_hol act_pub_hol birthday">Wkday, WA PH, ACT PH, Bday</td>          

#       <td class="weekend wa_pub_hol">Wknd and WA PH</td>
#       <td class="weekend act_pub_hol">Wknd and ACT PH</td>
#       <td class="weekend birthday">Wknd and Bday</td>
          
#       <td class="weekend wa_pub_hol birthday">Wknd, WA PH, Bday</td>
#       <td class="weekend act_pub_hol birthday">Wknd, ACT PH, Bday</td>
          
#       <td class="weekend wa_pub_hol act_pub_hol">Wknd, WA PH, ACT PH</td>
#       <td class="weekend wa_pub_hol act_pub_hol birthday">Wknd, WA PH, ACT PH, Bday</td>
#     </tr>
# """)

  f.write("""
    <tr class="noborder"><td colspan="12">&nbsp;</td></tr>
    <tr class="noborder"><td colspan="12">&nbsp;</td></tr>
    <tr>
      <td class="weekend">Weekend</td>
      <td class="birthday">Birthdays</td>
      <td class="wa_pub_hol">Perth Pub Hols</td>
      <td class="act_pub_hol">Canberra Pub Hols</td>
      <td class="school_hol_legend">School Hols</td>
    </tr>
""")
  f.write("</table>")

html = weasyprint.HTML("planner.html")
html.write_pdf(target="planner.pdf")