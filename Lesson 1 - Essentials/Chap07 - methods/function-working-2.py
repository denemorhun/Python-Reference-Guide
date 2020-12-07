#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
   kitten("roar", "grrr")

   x = "miyav"
   kitten(x, "horr")

   cat = kitten("ha", "ho")
   print(cat)

   print(*kitten_ages())

def kitten(*args):
    if len(args):
        for sound in args:
            print (sound)
    

def kitten_ages():
    return dict(x=42, y=43, z=44)
if __name__ == '__main__': main()
