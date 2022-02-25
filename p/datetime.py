import datetime
import pytz

d = datetime.date(1998, 7, 2) # (YYYY, MM, DD) it should be in this format
print(d)

tday = datetime.date.today() # current date
print(tday)

year = tday.year
month = tday.month
dy = tday.day
print(year)
print(month)
print(dy)

print(tday.weekday()) # Monday : 0 || Sunday : 6
print(tday.isoweekday()) # Monday : 1 || Sunday : 7

tmdelta = datetime.timedelta(days=7)
print(tday - tmdelta) # what date was on this day a week (7 days) ago
print(tday)
print(tday + tmdelta) # what date will in this day a week before

# date1 + timedelta = date2     # subtracting or adding a date with timedelta gives a new date
# date1 + date2 = timedelta     # subtracting or adding a date with another date gives timedelta

bday = tday - d     # will store number of days
print(bday)
print(bday.days)        # will print days
print(bday.total_seconds())     # will print total no. of seconds


# time

t = datetime.time(11, 28, 30, 100000)
print(t)
print(t.hour)
print(t.minute)
print(t.second)
print(t.microsecond)

dt = datetime.datetime(2022, 2, 13, 11, 31, 20, 100000)
print(dt)
print(dt.year)
print(dt.hour)

