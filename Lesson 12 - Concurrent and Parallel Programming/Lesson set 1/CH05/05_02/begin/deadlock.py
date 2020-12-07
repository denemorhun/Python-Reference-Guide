#!/usr/bin/env python3
""" Three philosophers, thinking and eating sushi """

import threading
import logging

chopstick_a = threading.Lock()
chopstick_b = threading.Lock()
chopstick_c = threading.Lock()
sushi_count = 500

def philosopher(name, first_chopstick, second_chopstick):
    global sushi_count

    logging.basicConfig(level=logging.DEBUG, filename="deadlock.log",
                            filemode = 'w')

    while sushi_count > 0: # eat sushi until it's all gone
        
        with first_chopstick:
            with second_chopstick:
                if sushi_count > 0:
                    sushi_count -= 1
                #  logging.info(name, 'took a piece! Sushi remaining:', sushi_count)
                    print(name, 'took a piece! Sushi remaining:', sushi_count)

if __name__ == '__main__':
    threading.Thread(target=philosopher, args=('Barron', chopstick_a, chopstick_b)).start()
    threading.Thread(target=philosopher, args=('Olivia', chopstick_b, chopstick_c)).start()
    threading.Thread(target=philosopher, args=('Steve', chopstick_a, chopstick_c)).start()