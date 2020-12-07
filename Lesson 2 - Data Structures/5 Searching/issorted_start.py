# determine if a list is sorted
# linear complexity - as items increase complexity is linearly incremented


items1 = [6, 8, 19, 20, 23, 41, 49, 53, 56, 87]
items2 = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]

def is_sorted(itemlist):
    # TODO: using the brute force method
    # create a loop that compares each item to the next to last one
    isSorted = True
    
    for i in range(0,len(items1)-1):
        #if any item is less than
        if (itemlist[i] > itemlist[i+1]):
            isSorted = False

    return isSorted

print(is_sorted(items1))
print(is_sorted(items2))

