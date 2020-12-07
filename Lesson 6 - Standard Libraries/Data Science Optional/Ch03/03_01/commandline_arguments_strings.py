# Command Line Arguments
import sys

# Print Arguments
print("Number of arguments: ", len(sys.argv), ' arguments.')
print("Arguments ", sys.argv)

# # Remove Arguments
# sys.argv.remove(sys.argv[0])

# print("Arguments", sys.argv)

# pick uption
arguments = sys.argv
for arg in arguments:
    try:
        if arg == 'pass':
            print('Calling pass function: ')
        elif arg == 'loc':
            print('Calling loc function')
        elif arg == 'people':
            print('Calling the people function')
        else:
            print('Option not supported.')
   
    except Exception:
        print("Bad input")
