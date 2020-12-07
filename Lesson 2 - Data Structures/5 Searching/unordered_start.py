# searching for an item in an unordered list
# sometimes called a Linear search

# declare a list of values to operate on
items = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]

def find_item(item, itemlist):
    # look for item in the length of the list
    for idx in range(0, len(itemlist)):
        # if item matches the value return its index
        if (item == itemlist[idx]):
            return idx
    
    return None


print(find_item(87, items))
print(find_item(250, items))
