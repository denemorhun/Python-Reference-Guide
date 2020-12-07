# use iterator functions like enumerate, zip, iter, next
import os
import sys

def main():
    # define a list of days in English and French
    days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    daysFr = ["Dim", "Lun", "Mar", "Mer", "Jeu", "Ven", "Sam"]

    # TODO: use iter to create an iterator over a collection

    i = iter(days)

    # TODO: iterate using a function and a sentinel
    # print(*i) -> prints the who list
    # fp = open(os.path.join(sys.path[0], "testfile.txt"))
    # for line in iter(fp.readline, ''):
    #     print(line.rstrip())


    # TODO: use regular iteration over the days
    # for day in i:
    #     print(day)

    # TODO: using enumerate reduces code and provides a counter
    print(*enumerate(i))
    for i,m in enumerate(days, start=1):
        print(i, m)

    # TODO: use zip to combine sequences
    for m in zip(days, daysFr):
        print(m)

    for i, m in enumerate(zip(days, daysFr), start=1):
        print(i, m[0], "=", m[1], "On Francais")

    print(list(enumerate(zip(days, daysFr), start=1)))

if __name__ == "__main__":
    main()
