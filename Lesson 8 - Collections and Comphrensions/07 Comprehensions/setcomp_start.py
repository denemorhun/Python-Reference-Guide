# Demonstrate how to use set comprehensions


def main():
    # define a list of temperature data points
    ctemps = [5, 10, 12, 14, 10, 23, 41, 30, 12, 24, 12, 18, 29]

    # TODO: build a set of unique Fahrenheit temperatures
    # ftemps = set(int(f*9/5+32) for f in ctemps)
    # print(type(ftemps))
    # print(sorted(ftemps))

    # TODO: build a set from an input source string
    tempStr = "The pigeon is living in the living room"
    chars = sorted(set(my_char.upper() for my_char in tempStr if not my_char.isspace()))
    print(chars)

if __name__ == "__main__":
    main()
