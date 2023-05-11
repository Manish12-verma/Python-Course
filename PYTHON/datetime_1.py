from datetime import date

today = date.today()
print("Today's date is", today)

print("date components:",today.day,today.month,today.year)
print ("today's weekday # is ",today.weekday())