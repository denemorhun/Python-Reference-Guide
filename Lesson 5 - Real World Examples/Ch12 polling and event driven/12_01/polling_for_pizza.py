""" Polling for Pizza to Cure My Hunger """

# with open(os.path.join(sys.path[0], "textfile.txt"), "w+") as f:
    #     for i in range(10):
    #         f.write("This is line number " + str(i) + "\r\n")

import os
import sys
import time

hungry = True  # I need a pizza!

while(hungry):

    print('Opening the front door')
    # front_door = open('front_door.txt', 'r')

    front_door = open(os.path.join(sys.path[0], "front_door.txt"), "r")

    if "Pizza Guy" in front_door:
        print("Pizza's here!")
        hungry = False;
    else:
        print("Not yet...")

    print('Closing the front door.')
    front_door.close()  
    
    #sleep 10 seconds to avoid hogging the system. 
    time.sleep(10)
