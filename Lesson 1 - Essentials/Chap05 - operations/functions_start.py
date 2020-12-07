#
# Example file for working with functions
#

# define a basic function
def func1():
    print("I am a function")


# function that takes arguments and sums it up
def sum2(arg1, arg2):
    print ("sum of the args is " + str(arg1+arg2))

# function that returns a value
def cube(x):
    print(x**3)
    return(x**3)

# function with default value for an argument
def power(num, x=1):
    print(num**x)
    return(num**x)

# function with default value for an argument with for loop

def powerLoop(num, y=1):
    result = 1
    for i in range(y):
        result = result * num
    return result

#function with variable number of arguments
def multi_add(*args):
    result = 0
    for i in args:
        result += i
    return result

# print output from the functions
print("Func1")
func1()
# print function def
print(func1)
# does not return anything
print(func1())

print("func2")
sum2(3,4)

print("func3")
cube(3)
print(cube(3))

print("func4")
(power(2))
print(power(2,4))

print("func5")
print(powerLoop(5, 0))
print(powerLoop(2, 3))
print(powerLoop(1,6))

print("func6")
print(multi_add(2, 66))