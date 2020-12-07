# Command Line Arguments
import sys

arguments = sys.argv

# Print Arguments
print("Number of arguments: ", len(arguments), ' arguments.')
print("List of arguments ", arguments)
print("Get name of script at argument[0]: ", arguments[0])

# remove first argument which is name of script
arguments.remove(arguments[0])

print("Arguments without script name: ", arguments)

# Sum up the Arguments
sum = 0
for arg in arguments:
    try:
        number = int(arg)
        sum = sum + number
    except Exception:
        print("Bad input")

print(sum)