""" Ordering A Pizza That Verne Can Eat """

from datetime import date

# get the day special
def day_special(specials):

    today = get_day_of_week()

    for day, topping in specials.items():
        if today.lower() == day.lower():
            return specials[day]

def get_day_of_week():
    days = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
    today = days[date.today().weekday()]
    return today

# list of specials available
specials = {'Sunday'    : 'spinach', 
            'Monday'    : 'mushroom', 
            'Tuesday'   : 'pepperoni', 
            'Wednesday' : 'veggie',
            'Thursday'  : 'bbq chicken',
            'Friday'    : 'sausage',
            'Saturday'  : 'Hawaiian'}


# things that Verne does not eat
diet_restrictions = set(['cheese', 'meat'])
# diet_restrictions = set(['fish'])

# decide which pizza to order      

if 'meat' in diet_restrictions:
    print("Get vegan pizza")  
elif "meat" and 'cheese' in diet_restrictions:
        print("Get vegaterian pizza")
elif 'cheese' in diet_restrictions:
    print("get a burger instead")
else:
    print("Get pepperoni and mushroom!")

print(f"Also order the {day_special(specials)} pizza on special!")