'''
Numbers are formed with closed paths. Digits 0, 4, 6, 9 have 1 closed path,
8 has 2.

Ex: number 649578

Digits with closed paths are 6, 4, 9, 8 -> 1 + 1 + 1 + 2 = 5

'''


def closedPaths(number) -> int:
    # count number of closed paths
    cp = 0

    while number > 0:
        # find last digit d
        d = number % 10

        # these numbers have cp of 1
        if(d == 0 or d == 4 or d == 6 or d == 9):
            cp += 1

        # 8 has cp of 2
        elif d == 8:
            cp += 2
        # remove last digit and repeat loop by dividing by 10
        number//=10

    return cp


print(closedPaths(649578))
print(closedPaths(6))
closedPaths(6666)
closedPaths(8888)

