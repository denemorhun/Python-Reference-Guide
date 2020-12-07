#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    animals = { 'kitten': 'meow', 'puppy': 'ruff!', 'lion': 'grrr',
        'giraffe': 'I am a giraffe!', 'dragon': 'rawr' }

    animals["monkey"] = "haha"
    animals["donkey"] = "brah"

    print("print key and values")
    for k,v in animals.items():
        print(f'Key is {k}, value is {v}')

    # print("keys only")
    # for k in animals.keys():
    #     print("Key", k)

    # print("values only")
    # for v in animals.values():
    #     print("Value", v)

    animal = "boar"
    print(f'{animal} exists' if animal in animals else 'Nope')

    print(f"Get {animal} sound: ", animals.get(animal))

   #  print_dict(animals)

def print_dict(o):
    for x in o: 
        print(f'{x}: {o[x]}')

if __name__ == '__main__': main()
