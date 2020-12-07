# Calendar Module
from datetime import datetime, timedelta

now = datetime.now()

td = now + timedelta(days=2)

print("now is " + now.strftime("%a %b %d %y"))

print(td.strftime("and the exam's on: " + "%a %b %d %y"))

time_since_my_first_lic = now - timedelta(weeks=3)
print(time_since_my_first_lic.strftime("I've been studying since " + "%a %b %d %y"))

