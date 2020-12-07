#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# Sample code to read input and write output:

'''
NAME = input()                # Read input from STDIN
print("Hello " + NAME)        # Write output to STDOUT
'''

# Warning: Printing unwanted or ill-formatted 
# data to output will cause the test cases to fail

def kthSmallestStock(array, n, k):
    #sort array
    array.sort()
    
    #return the value of the kth element in the sorted array

    print(n)
    return array[k-1]
    
if __name__ == 'main':
    main()


def main():

    arr = [5, 6, 10, 19, 88]
    
    n = len(arr)
    k = 3 
    
    print("Kth smallest element", kthSmallestStock(arr, n, k))


#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

if __name__ == '__main__': main()
