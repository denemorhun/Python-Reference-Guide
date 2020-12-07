#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
   print(kitten("roar", "grrr"))
   print(kitten())

   x = "miyav"
   print(kitten(x, "horr"))

def kitten(sound2 = " purr ", sound3 = " mrrr " ):
    sound3 = "isthismutable"
    print(sound3)
    return ('Meow' + " " + sound2 +  " " + sound3)
    

if __name__ == '__main__': main()
