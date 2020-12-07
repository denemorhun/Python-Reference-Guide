#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    game = [ 'Rock', 'Paper', 'Scissors', 'Lizard', 'Spock' ]
    print_list(game[1:4:1])
    i = game.index("Rock")
    print("Index for {} is {}".format(game[0],i))

    # to add items to the list
    game.insert(0,'Computer')
    print("Index for {} is {}".format(game[0],i))

     # to remove items
    game.remove('Scissors')
    if not game.__contains__('Scissors'):
        print("Scissors is gone!")

    print_list(game)
    
    # to pop items
    x = game.pop()
    print("Popped value", x)
    print_list(game)

    # to remove at an idx
    del game[0]
    print_list(game)

    y = game.pop(0)
    print(y)
    print_list(game)

def print_list(o):
    print("Game is now: ")
    for i in o: print(i, end=' ', flush=True)
    print()

if __name__ == '__main__': main()
