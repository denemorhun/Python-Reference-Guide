# 0 1 1 2 3 5 8
# f0 -> 0
# f(1)-> 0, 1
# f(2) -> 0, 1, 1
# f3 -> 0, 1, 1, 2

# however, traditionally f1 is f0, 
def fib(n):

	if n < 0:
		retun 0
	if n == 1:
		return 0
	elif n == 2:
		return 1
	else:
		return (fib(n-1) + fib(n-2))

def test_fib():
	assert fib(5) == 3


# first valid input is 1
for i in range(1,10):
	print(f'input {i}, fib num {fib(i)}')
