# Demonstrate the use of function docstrings


def myFunction(arg1, arg2=None):
    """
    myFunction(arg1, arg2=None) -> just print

    Parameters:
    arg1: the first argument
    arg2: the second argument

    """
    print(arg1, arg2)


def main():
    print(myFunction.__doc__)


if __name__ == "__main__":
    main()
