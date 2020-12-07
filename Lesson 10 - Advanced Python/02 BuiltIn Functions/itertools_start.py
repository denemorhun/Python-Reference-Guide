# advanced iteration functions in the itertools package
import itertools

def testFunction(x):
    return x < 40

def cube3(x):
    return x**3

def main():
    # TODO: cycle iterator can be used to cycle over a collection indefinetely
    # seq1 = ["Joe", "John", "Mike"]
    # cycle1 = itertools.cycle(seq1)
    
    # i = 0
    # while i < 4:
    #     print(next(cycle1))
    #     i += 1

    # TODO: use count to create a simple counter, careful, its infinite
    # for x in itertools.count(1, 10):
    #     print(x)
    #     if x > 100:
    #         break

    # TODO: use map and count to generate a sequence
    # i = 0
    # while i < 100:
    #     y = map(cube3, itertools.count(1, 5))
    # print(list(y))

    # TODO: accumulate creates an iterator that accumulates values
    # vals = [10,20,30,40,50,40,30]
    # acc = itertools.accumulate(vals, max)
    # print(list(acc))
    # output [10, 20, 30, 40, 50, 50, 50]
            
    # TODO: use chain to connect sequences together
    # seq1 = [1,2,3,4]
    # seq2 = [5,6,7,8]

    # comb = itertools.chain(seq1, seq2)
    # print(list(comb))
    
    # TODO: dropwhile and takewhile will return values until
    # a certain condition is met that stops them
    vals = [10,20,30,40,50,40,30]
    print("values are", *vals)
    print(list(itertools.dropwhile(testFunction, vals)))
    print(list(itertools.takewhile(testFunction, vals)))

    
if __name__ == "__main__":
    main()
    