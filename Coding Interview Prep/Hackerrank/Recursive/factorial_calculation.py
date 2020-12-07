'''
Python3 code to calculate factorial
'''

def calculate_factorial(n) -> int:

        # base condition 
        if n < 2:
            return 1
        else:
            return n * calculate_factorial(n-1)

def calculate_factorial_iterative(n) -> int:
    i = 0
    fact = 1
    while i < n:
        fact *= n-i
        i+=1
    return fact

if __name__ == '__main__':
        n = 4

        #print(calculate_factorial(n))
        print(calculate_factorial_iterative(n))