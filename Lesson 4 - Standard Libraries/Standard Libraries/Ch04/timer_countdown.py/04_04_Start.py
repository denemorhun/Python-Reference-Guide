# Create a Timer with the Time module
import time

seconds = 0

seconds = int(input(seconds))
print(seconds)

while (int(seconds) > 0):
    try:
        time.sleep(1)
        seconds -= 1
    except TimeoutError:
        print("io exception")