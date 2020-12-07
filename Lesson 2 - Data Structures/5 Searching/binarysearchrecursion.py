# searching for an item in an ordered list
# this technique uses a binary search
# didnt work - revisit later

def binarysearch(value, items):
    left = 0
    right = len(items) - 1

    if left <= right:
        middle = (left + right) // 2

        if items[middle] == value:
            return middle

        elif items[middle] < value:
            return binarysearch(value, items[middle + 1])
        elif items[middle] > value:
            return binarysearch(value, items[middle-1])

    return None


items = [6, 8, 19, 20, 23, 41, 49, 53, 56, 87]

print('index should be 4, is', binarysearch(23, items))
print('index should be 7, is', binarysearch(53, items))
print('index should be 9, is', binarysearch(87, items))
print('index should be None, is', binarysearch(250, items))
