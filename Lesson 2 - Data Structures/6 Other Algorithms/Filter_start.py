# use a hashtable to filter out duplicate items
# o(n) complexity

# define a set of items that we want to reduce duplicates
items = ["apple", "pear", "orange", "banana", "apple",
         "orange", "apple", "pear", "banana", "orange",
         "apple", "kiwi", "pear", "apple", "orange"]

# TODO: create a blank hashtable to perform a filter
filter = {}

# TODO: loop over each item and add items as keys to the hashtable
# assign any value (0), it won't be used
for item in items:
    filter[item] = 0
    
print(filter)
# {'apple': 0, 'pear': 0, 'orange': 0, 'banana': 0, 'kiwi': 0}

# TODO: create a set from the resulting keys in the hashtable

results  = set(filter.keys())
print(results)
# {'banana', 'pear', 'kiwi', 'orange', 'apple'}