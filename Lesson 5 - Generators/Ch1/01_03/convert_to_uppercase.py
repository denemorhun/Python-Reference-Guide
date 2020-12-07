# convert to lower case and reverse

def reverse(x):
    return x[::-1]

names_list = ['Adam','Anne','Barry','Brianne','Charlie','Cassandra',
    'David','Dana']

#Converts names to lower
lower_names = list((name.lower() for name in names_list))

print(reverse(lower_names))

print(sorted(list('denem')))


print(reverse(['a','b','c']))

