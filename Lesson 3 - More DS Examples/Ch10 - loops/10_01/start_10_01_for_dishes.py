""" Loading the Dishwasher """

# dirty dishes in the sink
sink = ['bowl','plate','cup']

# we need to do list
for dish in list(sink):
    print('Putting {} in the dishwasher'.format(dish))
    sink.pop()

print(*sink)

