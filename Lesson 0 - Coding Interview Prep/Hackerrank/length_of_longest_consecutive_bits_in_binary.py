# Convert decimal to binary
# count length of the longest consecutive bits
'''
if we a bitwise AND with a bit sequence of a shifted version of itself,
we’re removing the trailing 1 from every sequence of consecutive 1s.

      11101111   (x)
    & 11011110   (x << 1)
    ----------
      11001110   (x & (x << 1)) 
        ^    ^
        |    |
   trailing 1 removed

The operation x = (x & (x << 1)) reduces length of every 
sequence of 1s by one in binary representation of x. 
If we repeat this operation in a loop, we end up with x = 0. 

The number of iterations required to reach 0 is length of the 
longest consecutive sequence of 1s.
'''

from typing import ByteString

def convert_to_binary(n) -> int:
    stack = []
    while n > 0:
        remainder = n % 2
        stack.append(remainder)
        n = n // 2

    stack.reverse()
    return convert_list_to_string(stack)

def convert_list_to_string(arr):
    return "".join(map(str, arr))

def count_max_consecutive_bits(n):
    count = 0

    # Count the number of iterations to 
    # reach x = 0.
    while n != 0:
        # This operation reduces length 
        # of every sequence of 1s by one. 
        n = n & (n << 1)
        count += 1

    return count

# driver code
def main():
        input = 300
        print(count_max_consecutive_bits(input))
        print(convert_to_binary(input))

if __name__ == '__main__': main()
