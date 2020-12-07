# generator solution
def even_integers_generator(n):
    for i in range(n):
        if i % 2 == 0:
            yield i

# c = 0
# num = 10
# gen = even_integers_generator(10)

# using the next()
# while c < 10:
#     print(next(i))
#     c += 1

# for loop:
# for even in gen:
#     print(even)

# for loop 2nd method to get even numbers
for n in even_integers_generator(10):
    print(n)

# get max: 9
print(max(i for i in range(10)))
