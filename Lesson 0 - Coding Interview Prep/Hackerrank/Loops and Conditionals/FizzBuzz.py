# EASY
'''
prints each number from 1 to 100 on a new line. 

For each multiple of 3, print "Fizz" instead of the number. 

For each multiple of 5, print "Buzz" instead of the number. 

For numbers which are multiples of both 3 and 5, print "FizzBuzz" instead of the number.
'''

def FizzBuzz():

    i = 1
    
    while (i <= 100):
            if (i % 5 == 0 and i % 3 != 0):
                print ("Buzz")
            elif (i % 3 == 0 and i % 5 != 0):
                print("Fizz")
            elif (i % 15 == 0):
                print("FizzBuzz")
            else:
                print(i)

            i += 1

if __name__ == '__main__':
        FizzBuzz()