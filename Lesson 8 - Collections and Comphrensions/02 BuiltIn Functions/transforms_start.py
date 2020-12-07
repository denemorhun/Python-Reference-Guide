# use transform functions like sorted, filter, map

import collections

# method to filter out even numbers
def oddFilter(x):
    if x % 2 == 0:
        return False
    return True

# method to filter out lower case characters
def noLowerFilter(x):
    if str.islower(x) is True:
        return False
    return True

def squareFunc(x):
    return pow(x, 2)

def toGrade(x):
    if x >= 90:
        return 'A'
    elif x < 90 and x >= 80 :
        return 'B'
    elif x < 80 and x >= 70:
        return 'C'
    elif x < 70 and x >= 60:
        return 'D'
    return 'F'

def main():
    # define some sample sequences to operate on
    nums = (1, 8, 4, 5, 13, 26, 381, 410, 58, 47)
    chars = "abcDeFGHiJklmnoP"
    grades = (81, 89, 94, 78, 61, 66, 99, 74)

    # TODO: use filter to remove odd items from a list
    odds = list(filter(oddFilter, nums))
    print(odds)

    # TODO: use filter on non-numeric sequence
    # print(list(filter(str.isupper, chars)))
    uppers = list(filter(noLowerFilter, chars))
    print(uppers)

    # TODO: use map to create a new sequence of values
    sqs = list(map(squareFunc, range(0,10)))
    print(sqs)

    # TODO: use sorted and map to change numbers to grades
    grades = sorted(grades, reverse=True) 
    letter_grades = list((map(toGrade, grades)))
    c = collections.Counter(letter_grades)
    print(c)

if __name__ == "__main__":
    main()
