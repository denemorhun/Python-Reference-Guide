from collections import Counter 

x = ['cat', 'dog', 'rabbit', 'raptor', 'raptor', 'raptor']
print(*enumerate(x))

seen = Counter(x)
print(seen, *seen.values())
#cat dog rabbit raptor 1 1 1 3

print(seen['cat'])
print(x.count('cat') )
# 1

print ('cat' in x)
# true