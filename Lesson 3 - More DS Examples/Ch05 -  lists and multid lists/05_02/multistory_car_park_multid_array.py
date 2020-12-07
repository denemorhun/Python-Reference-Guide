""" A 3-Dimensional Valet Service """

# 2D list of lists
#  - index cars by row, spot
lot_2d = [['Toyota','Audi','BMW'], # 0th row
          ['Lexus','Jeep'],        # 1st row
          ['Honda','Kia','Mazda']] # 2nd row

# print a single car
print(lot_2d[1][1])
# Jeep

# 1D array 
lot_1d = ['Toyota','Audi','BMW']

# idx = 0

# for car in lot_1d:
#         print (f"Your car {car} is at spot {idx}")
#         idx += 1


# # 2D array
print('2D array example')

# row_idx = 0 
# for row in lot_2d:
#     for car in row:
#         print (f"Your car {car} is at row {row_idx} and spot", row.index(car))
#     row_idx += 1

print('3d array example')
# 3D list of lists of lists
# - index cars by floor, row, spot
lot_3d = [[['Tesla','Fiat','BMW','Ferrari'], 
           ['Honda','Jeep'],
           ['Saab','Kia','Ford']], #0th floor

          [['Subaru','Nissan'], ['Volvo']],  # 1st floor

          [['Mazda','Chevy'],[], ['Volkswagen']]]  # 2nd floor

print(lot_3d)

# # Print all cars
f = 0
for floor in lot_3d:
    r = 0
    for row in floor:
        for car in row:
            print (f"Your car {car} is at floor {f}, row {r+1} and spot", row.index(car)+1)
        r += 1
    f += 1 