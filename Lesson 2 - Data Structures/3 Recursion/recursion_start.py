# Using recursion to implement power and factorial functions

# if n is even power(x,n) =power(x,n/2)*power(x,n/2)
# else n is odd power(x,n)=x*power(x,n/2)*power(x,n/2)
def power(num, pwr):
#base condition
    if pwr == 0:
        return 1
    else:
        return num * power(num, pwr-1)


def factorial(num):
    #0! is 1
    if num == 0:
        return 1
    else:
        return num*factorial(num-1)



print("{} to the power of {} is {}".format(5, 3, power(5, 3)))
print("{} to the power of {} is {}".format(1, 5, power(1, 5)))
print("{}! is {}".format(4, factorial(4)))
print("{}! is {}".format(0, factorial(0)))
