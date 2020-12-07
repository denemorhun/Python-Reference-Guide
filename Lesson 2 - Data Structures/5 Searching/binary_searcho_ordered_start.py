# searching for an item in an ordered list
# this technique uses a binary search



def binarysearch(value, items):

    items = sorted(items)
    
    # start at the two ends of the list
    left = 0
    right = len(items) - 1

    while left <= right:
        # TODO: calculate the middle point
        middle = (left + right) // 2

        # TODO: if item is found, return the index
        if (value == items[middle]):
            return middle
        # TODO: otherwise get the next midpoint
        # move lower index past midpoint if searched item is greater
        elif (value > items[middle]):
            left = middle + 1
        #move upper index before midpoint if searched item is less
        elif (value < items[middle]):
            right = middle - 1

        # index doesn't exist
        if left > right:
            return None

# driver code            

items = [8, 20, 19, 23, 41, 49, 53, 56, 87, 5]

#we have to sort the array first. 

print('index should be 4, is', binarysearch(23, items))
print('index should be 7, is', binarysearch(53, items))
print('index should be 9, is', binarysearch( 87, items))
print('index should be None, is', binarysearch(250, items))
