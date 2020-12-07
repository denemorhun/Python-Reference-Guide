""" A Queue of Groceries to Put Away """

# create a new queue object
import queue as q

gro = q.Queue()
print("The groceries are empty" if gro.empty() else " groceries are full")

# put bags into the queue
gro.put_nowait("bag1")
gro.put_nowait("bag2")
gro.put_nowait("bag3")

# get bags from the queue in FIFO order
while not gro.empty():
    print(gro.get())


# q.get() # causes an error
# gro.get_nowait()

# create a new queue to hold two items - such as amazon locker
al = q.Queue(2)
# put two bags into the two-item queue
al.put("bag4")
al.put("bag5")

# prints the first item, bag4
print(al.get())


# try to put an extra bag into the queue
# al.put_nowait('bag3') # causes an error, queue full

al.put_nowait("bag6")
