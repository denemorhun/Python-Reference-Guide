# 0 1 1 2 3 5 8
# f0 -> 0
# f(1)-> 0, 1
# f(2) -> 0, 1, 1
# f3 -> 0, 1, 1, 2

# however, traditionally f1 is f0

# remember the two values, trail and lead


def fib():
    # base condition
    trail, lead = 0, 1
    while True:
        yield lead
        trail, lead = lead, lead + trail

# next(fib())

#create a new generator objects
fib = fib()
# print(next(fib))
# print(next(fib))
# print(next(fib))


# # first valid input is 1
for i in range(0, 5):
    print('input',i, 'fib num', next(fib))


# def test_fib():
#     assert fib(0) == 3


def fibonacci_starting_with_0(n):
   trail, lead = 0, 1

   for i in range (trail, n):
        yield trail
        trail, lead = lead, lead + trail


