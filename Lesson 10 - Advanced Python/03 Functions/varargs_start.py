# Demonstrate the use of variable argument lists


# TODO: define a function that takes variable arguments
def addition(*args):
    return sum(args)

def multiply(*args):
    result = 1
    for arg in args:
        result *= arg 
    return result


def main():
    # TODO: pass different arguments
    print(addition(1,2,3,4))
    print(multiply(1,2,3))

    # TODO: pass an existing list
    my_list = (1,2,3,4,5,6)
    print(addition(*my_list))
    print(multiply(*my_list))


if __name__ == "__main__":
    main()
