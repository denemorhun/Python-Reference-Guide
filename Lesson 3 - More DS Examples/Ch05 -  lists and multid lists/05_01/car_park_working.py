""" Parking Cars in a List using linked list """

# create a list of cars
row = ['Ford','Audi','BMW','Lexus']

# park my Mercedes at the end of the row

row.append('Mercedes')

print(row)
print(row[4])

# swap the BMW at index 2 for a Jeep

row[2] = 'Jeep'
print(row)

# park a Honda at the end of the row
row.append('Honda')
print(row)
print(row[4])

# park a Kia at the front of the row

row.insert(0, 'Kia')
print(row)
print(row[4])

# find my Mercedes's index and leave the list

idx = row.index('Mercedes')
print(f"my car is at spot: {idx}")
my_car = row.pop(idx)
print(f"My car {my_car} is leaving!")
print(row)

# find and remove the Lexus

row.remove('Lexus')

print(row)
