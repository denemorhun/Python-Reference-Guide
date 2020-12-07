#!/usr/bin/env python3
""" Two threads chopping vegetables """

import threading
import time

chopping = True
seasoning = True

def meat_seasoner():
    name = threading.current_thread().getName()
    meat_count = 0
    while seasoning:
        print(name, 'seasoned a sausage')
        meat_count += 1
    print(name, 'seasoned', meat_count, 'sausages')

def vegetable_chopper():
    name = threading.current_thread().getName()
    vegetable_count = 0
    while chopping:
        print(name, 'chopped a vegetable!')
        vegetable_count += 1
    print(name, 'chopped', vegetable_count, 'vegetables.')

if __name__ == '__main__':
    threading.Thread(target=vegetable_chopper, name='Barron').start()
    threading.Thread(target=vegetable_chopper, name='Olivia').start()
    threading.Thread(target=meat_seasoner, name='Denem').start()

    time.sleep(1)    # chop vegetables for 1 second
    chopping = seasoning = False # stop both threads from chopping
