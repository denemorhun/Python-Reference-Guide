#!/usr/bin/env python3
""" Two shoppers adding items to a shared notepad """

import threading

garlic_count = 0

def shopper():
    global garlic_count
    for i in range(10):
        garlic_count += 1

def bagger():
    print("bagging the garlic")

if __name__ == '__main__':
    barron = threading.Thread(target=shopper)
    olivia = threading.Thread(target=shopper)
    bagger = threading.Thread(target=bagger)

    barron.start()
    olivia.start()

    bagger.start()

    barron.join()
    olivia.join()

    bagger.join()
    print('We should buy', garlic_count, 'garlic.')
