r = range(0,30)
print(type(r))

x =  'denem'


if type(x) is str:
    print(x + ' is of type' + str(type(x)))

class Car:
    print("I'm a car")
    pass


class Truck(Car):
    print("I'm a truck")
    pass

c = Car()
print(type(c))

t = Truck()
print(type(t))

benz = Car()

print(type(benz) == type(c))

# The following statements both check the type
print(type(c) == Car)
print(isinstance(c, Car))
print(isinstance(t, Car))