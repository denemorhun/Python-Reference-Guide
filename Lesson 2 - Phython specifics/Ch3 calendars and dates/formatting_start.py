#
# Example file for formatting time and date output
#

from datetime import datetime

def main():
  # Times and dates can be formatted using a set of predefined string
  # control codes 

  #### Date Formatting ####
  
  now = datetime.now()
  
 
  # %y/%Y - Year, %a/%A - weekday, %b/%B - month, %d - day of month
  print(now.strftime("Current year is: %Y"))
  print(now.strftime("Current weekday is: %A"))
  print(now.strftime("Current month is: %B"))
  print(now.strftime("Current date is: %d"))

  # %c - locale's date and time, %x - locale's date, %X - locale's time
  print(now.strftime("Current local date and time is: %c"))
  print(now.strftime("Current local date is: %x"))
  print(now.strftime("Current local date is: %X"))


  #### Time Formatting ####
  
  # %I/%H - 12/24 Hour, %M - minute, %S - second, %p - locale's AM/PM



if __name__ == "__main__":
  main();
