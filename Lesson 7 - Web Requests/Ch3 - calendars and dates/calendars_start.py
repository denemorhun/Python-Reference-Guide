#
# Example file for working with Calendars
#

# import the calendar module
import calendar

#####################################################################
# Calculate days based on a rule: For example, consider
# a team meeting on the first Monday of every month.
# To figure out what days that would be for each month
#####################################################################
def get_meeting_days(year):
    print ("Team meetings will be on:")

    # create calendar with 12 months
    for m in range(1,13):
    # returns an array of weeks that represent the month
    # weeks themselves are arrays of days
        cal = calendar.monthcalendar(2020, m)

    # The first Monday has to be within the first two weeks
        week_one = cal[0]
        week_two = cal[1]

        # if day doesn't fall within the week, 0 is printed
        if week_one[calendar.MONDAY] != 0:
            meetday = week_one[calendar.MONDAY]
        else:
        # if the first friday isn't in the first week, it must be in the second
            meetday = week_two[calendar.MONDAY]
      
        print ("%10s %2d" % (calendar.month_name[m], meetday))

get_meeting_days(2020)


#############################################################################
# various calendar related commands
############################################################################

# create a plain text calendar that begins with Sunday, default monday
# c = calendar.TextCalendar(calendar.SUNDAY)

# format calendar into a string
# st = c.formatmonth(2020,8,0,0)
# print(st)

# create an HTML formatted calendar

# htmlc = calendar.HTMLCalendar(calendar.MONDAY)
# st = htmlc.formatmonth(2020,8)
# print(st)

# loop over the days of a month
# zeroes mean that the day of the week is in an overlapping month
# for day in c.itermonthdays(2020,8):
#     print(day)
  
# The Calendar module provides useful utilities for the given locale,
# such as the names of days and months in both full and abbreviated forms
# for name in calendar.month_name:
#     print(name)

# for day in calendar.monthrange(2008, 7):
#     print(day)