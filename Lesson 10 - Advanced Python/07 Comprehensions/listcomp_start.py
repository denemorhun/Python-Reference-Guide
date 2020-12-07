# Demonstrate how to use list comprehensions

def main():
    # define two lists of numbers
    evens = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

    # TODO: Perform a mapping and filter function on a list
    # produce the squares of the lists

    # using lambda
    evensquared = list(map(lambda i: i**2, 
                      filter(lambda e: e > 4 and e < 16, evens)))
    print(evensquared)

    # using list comprehension
    evensquared_lc = [i**2 for i in evens if (i > 4 and i < 16)]
    print(evensquared_lc)

   

    # TODO: Derive a new list of numbers frm a given list
    # TODO: Limit the items operated on with a predicate condition
    # print the list of numbers divisible by 3
    odds_filtered = [i for i in odds if ( i % 3 == 0)]
    print(odds_filtered)

if __name__ == "__main__":
    main()
