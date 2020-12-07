''' Python program to find second largest number in a list
 
# list of numbers - length of 
# list should be at least 2

A general approach is to find the largest value of the dictionary and
 then iterate over the dictionary maintaining the value that must be greater
 than all the other values and less than the maximum value.
 '''


def find_2nd_largest_element(arr):

    # get max value

    max_value = max(arr)
    print(max_value)

    max2 = 0

    # iterate through array and replace max2 if value is larger
    for value in arr:
        if value < max_value and value > max2:
            max2 = value

    print(max2)


def main():
    inputString = [10, 20, 4, 45, 99]

    find_2nd_largest_element(inputString)


if __name__ == '__main__': main()
