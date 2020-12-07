#
# Example file for working with timedelta objects
#

from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

# store now
now = datetime.now()

# construct a basic timedelta and print it
print("timedelta", timedelta(days=365,hours=5,weeks=1,seconds=699))


# print today's date
print("Now is", now.strftime("%A %d %B %y"))

# print today's date one year from now

future = now + timedelta(days=365,hours=6)
print(future.strftime("1 year from now: %A %d %B %y"))

# calculate the date 1 week ago, formatted as a string
t = datetime.now() - timedelta(weeks=1)
print("One week before this", t.strftime("%a %d %B %y"))

### How many days until April Fools' Day?
today = date.today()
print(today)
afd = date(year=today.year, month=4, day=1)


# use date comparison to see if April Fool's has already gone for this year
# if it has, use the replace() function to get the date for next year
if today > afd:
    print("April fools day went by ", today - afd, " days ago")
    afd = afd.replace(year=today.year+1)

print (afd.strftime("New AFD is %Y %A %D %B "))


# Now calculate the amount of time until April Fool's Day  

days_till_afd = afd - today
print(days_till_afd)