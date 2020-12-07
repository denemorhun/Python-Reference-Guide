# using a hashtable to count individual items

# define a set of items that we want to count
items = ["apple", "pear", "orange", "banana", "apple",
         "orange", "apple", "pear", "banana", "orange",
         "apple", "kiwi", "pear", "apple", "orange"]

# TODO: create a hashtable object to hold the items and counts
counter = dict()

# TODO: iterate over each item
# increment the count for each one if already in system
for item in items:
    # first time we encounter it
    if item not in counter.keys(): 
        counter[item] = 1
    else:
        #increment the value for counter by 1
        counter[item] += 1

# print the results
print(counter)
#{'apple': 5, 'pear': 3, 'orange': 4, 'banana': 2, 'kiwi': 1}