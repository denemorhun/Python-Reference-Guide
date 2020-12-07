
# find the greatest common denominator for two numbers
# using euclid's algorithm

# for two integers where a > b, divide a by b
# if the remainder r = 0, stop, b is GCD

def gcd(a, b):
    while (b != 0):
        t = a
        a = b
        b = t % b
    return a

print(gcd(6, 2))
print(gcd(17, 2))
print(gcd(10, 5))
print(gcd(50, 15))