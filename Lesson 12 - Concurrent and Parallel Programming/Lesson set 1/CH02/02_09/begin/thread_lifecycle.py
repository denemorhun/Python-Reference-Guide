#!/usr/bin/env python3
""" Two threads cooking soup """

import threading
import time

class ChefDenem(threading.Thread):
    def __init__(self):
        super().__init__()

    def run(self):
        print('Denem is going to help with the sauce')
        time.sleep(2)
        print('Denem is done with the sauce')


class ChefOlivia(threading.Thread):
    def __init__(self):
        super().__init__()

    def run(self):
        print('Olivia started & waiting for sausage to thaw...')
        time.sleep(3)
        print('Olivia is done cutting sausage.')

# main thread a.k.a. Barron
if __name__ == '__main__':
    print("Barron started & requesting Olivia's help.")
    olivia = ChefOlivia()

    print('Barron is asking Denem to make the sauce')
    denem = ChefDenem()

    print('Barron asks Denem to prep the sauce')
    denem.start()
    denem.join()

    print('Barron tells Olivia to explicitly start.')
    olivia.start()

    print('Barron continues cooking soup.')
    time.sleep(0.5)

    print('Barron patiently waits for Olivia and Denem to finish and join...')
    olivia.join()
   
    print('Barron and Olivia and Denem are all done!')
