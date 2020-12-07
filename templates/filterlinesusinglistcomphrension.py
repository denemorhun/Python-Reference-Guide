#open file and filter

fh = open("input.txt", "r")

result = [i for i in fh if "line3" in i]
print(result)

string = "Hello 12345 World"
numbers = [x for x in string if x.isdigit()]
print (numbers)

numbers = [x for x in string if x.isalpha()]
print (numbers)