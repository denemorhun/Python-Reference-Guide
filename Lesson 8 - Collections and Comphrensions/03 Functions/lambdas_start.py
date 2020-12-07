# Use lambdas as in-place functions


def CelsisusToFahrenheit(temp):
    return int((temp * 9/5) + 32)


def FahrenheitToCelsisus(temp):
    return int((temp-32) * 5/9)


def main():
    ctemps = [0, 12, 21, 34, 100]
    ftemps = [32, 65, 70, 100, 212]

    # TODO: Use regular functions to convert temps
    print(list(map(lambda t: int((t-32) * 5/9), ftemps)))
    print(list(map(lambda t: int((t*9/5 + 32)), ctemps)))


    # TODO: Use lambdas to accomplish the same thing
    print(list(map(FahrenheitToCelsisus, ftemps)))
    print(list(map(CelsisusToFahrenheit, ctemps)))


if __name__ == "__main__":
    main()
