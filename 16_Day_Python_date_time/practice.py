from datetime import datetime
from datetime import timedelta

today = datetime.now()
print(today)
day, month, year, hour, minute, timestamp = today.day,today.month,today.year, today.hour,today.minute,today.timestamp()

# print(day, month, year, hour, minute, timestamp)

format_date = today.strftime("%m/%d/%Y, %H:%M:%S")
print(format_date)

date = '5 December, 2019'
date_obj = datetime.strptime(date,"%d %B, %Y")

from datetime import date

# Use date() to define specific calendar dates
t2 = date(1970, 1, 1)   # New Year's Day
t1 = date(2026, 7, 22)   # Today

# Subtract early date from later date
days_until_new_year = (t2 - t1).days

print(f"Time until New Year: {days_until_new_year} days")
