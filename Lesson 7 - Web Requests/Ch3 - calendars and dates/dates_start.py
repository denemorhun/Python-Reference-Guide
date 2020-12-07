#
# Example file for working with date information
#

from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

def main():
  # ## DATE OBJECTS
  # # Get today's date from the simple today() method from the date class
  # day = date.today()
  # print("Todays date is", day)

  # # print out the date's individual components
  # print("Date is broken down", "day", day.day, "month", 
  #       day.month, "year", day.year)
  
  # # retrieve today's weekday (0=Monday, 6=Sunday)
  # # use hashmap instead of switch statement

  # # store the number corresponding to the day
  # dayString = day.weekday()
  
  # # create a hashmap with values
  # switcher = {
  #       0: "Monday",
  #       1: "Tuesday",
  #       2: "Wed",
  #       3: "Th",
  #       4: "Fr",
  #       5: "Sat",
  #       6: "Sun"
  #   }

  # get value from hashmap with value from day
 # print(switcher.get(dayString))

  ## DATETIME OBJECTS
  # Get today's date from the datetime class
  # dayDT = datetime.now()
  # print(dayDT.strftime("%d-%B-%Y %H:%M:%S"))
  # 01-May-2020 16:16:24
  # print("DayDT", dayDT)


#   # Get the current time
#   print("Time is", dayDT.hour, dayDT.minute)
#   t = datetime.time(datetime.now())
#   print(t)

  # Get tomorrow's date
  today=date.today()
  tomorrow2 = today+timedelta(days=1)
  print(tomorrow2)

  tomorrow = date(year=today.year,month=today.month,day=today.day+1 )
  print(tomorrow)
  
if __name__ == "__main__":
  main();
  