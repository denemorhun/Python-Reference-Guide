
#list of mixed format numbers
numbers = [7, 22, 4.5, 99.7, '3', '5']

#convert numbers to integers using expression
integers = sorted(list((int(n) for n in numbers)))

print(integers)