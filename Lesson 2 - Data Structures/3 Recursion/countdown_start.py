# use recursion to implement a countdown counter


def countdown(x):
    if x == 0:
        print("done!")
    else:
        print(x)
        return countdown(x-1)


countdown(5)
