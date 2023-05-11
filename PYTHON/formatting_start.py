from datetime import datetime

now = datetime.now()
print(now.strftime("the current year is: %Y"))
print(now.strftime("%A,%d , %B , %y"))