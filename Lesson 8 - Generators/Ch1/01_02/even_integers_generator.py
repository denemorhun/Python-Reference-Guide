# generator solution
def even_integers_generator(n):
    for i in range(n):
        if i % 2 == 0:
            # this produces a generator instead of returning a value
            yield i


# if we don't have list, then we'll just print out gen object
print((even_integers_generator(10)))

# if we don't have list, then we'll just print out gen object
print(list(even_integers_generator(10)))

evens = even_integers_generator(10)

# output: <class 'generator'>
# print(type(evens))

# the following does the same thing, print 0 2 4 6 8
print(*evens)

for i in evens:
    print(i)

