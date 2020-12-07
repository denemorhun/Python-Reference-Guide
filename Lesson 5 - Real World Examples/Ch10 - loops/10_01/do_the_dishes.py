""" Loading the Dishwasher """

import random as r
# dirty dishes in the sink
sink = ['bowl','plate','cup']

# we need to do list
for dish in list(sink):
    print('Putting {} in the dishwasher'.format(dish))
    sink.pop()

print(*sink)

# finish items not washed in dishwasher
dirty = True
scrub_count = r.randint(1,4)
print(f"Need to wash {scrub_count} times")
while dirty:
    print("Scrub")
    print("Rinse")
    if scrub_count == 0:
        print("Done!")
        dirty = False
    
    scrub_count -= 1
        
    
