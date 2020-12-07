""" A Rolodex Full of Friends """

def caller_id(lookup_num):
    for name, num in rolodex.items():
        if lookup_num == num:
            return name

# dictionary of name/number pairs
rolodex = {'Aaron'  : 5556069,
           'Bill'   : 5559824,
           'Dad'    : 5552603,
           'Mom'    : 5552603,
           'David'  : 5558331,
           'Dillon' : 5553538,
           'Jim'    : 5555547,
           'Mom'    : 5552603,
           'Olivia' : 5556397,
           'Verne'  : 5555309}

rolodex['Amanda'] = 44444444
print(rolodex.get('Aaron'))

rolodex['Dad'] = 5
# print(hash('Dad'))

print(rolodex.get('Dad'))

# names = list(rolodex.keys())
# print(*names)

print(caller_id(5556397))
# returns Olivia

# what about mom and dad if they both have same number
print(caller_id(5552603))

