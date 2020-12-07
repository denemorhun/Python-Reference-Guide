# customize string representations of objects
# by overriding _repr_ _byte_ and _str_ functions


class Person():
    def __init__(self):
        self.fname = "Denem"
        self.lname = "Orhun"
        self.age = 37

    # TODO: use __repr__ to create a string useful for debugging
    def __repr__(self):
        return f'<Person Class - fname:{self.fname}, lname:{self.lname}, age: {self.age}>'


    # TODO: use str for a more human-readable string
    def __str__(self):
        return f'This person {self.fname} {self.lname} is {self.age} years old.'

    def __bytes__(self):
        person_str = f'This person {self.fname} {self.lname} is {self.age} years old.'
        return bytes(person_str.encode('utf-8'))

def main():
    # create a new Person object
    cls1 = Person()

    # use different Python functions to convert it to a string
    print(repr(cls1))
    print(str(cls1))
    print("Formatted: {0}".format(cls1))

    cls2 = Person()
    print(bytes(cls2))

if __name__ == "__main__":
    main()
