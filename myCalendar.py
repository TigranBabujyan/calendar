import calendar
import datetime

cur_datetima =  datetime.datetime.now()
year = cur_datetima.year
month = cur_datetima.month

print (calendar.month(year,month))
# print(calendar.calendar(year))