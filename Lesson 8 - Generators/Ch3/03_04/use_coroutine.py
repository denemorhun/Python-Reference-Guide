from coroutine_decorator import coroutine_decorator

def sender(filename, target):
    for line in open(filename):
        target.send(line)
    target.close()
        

@coroutine_decorator
def match_counter(str):
    count = 0
    try:
        while True:
            line = yield
            if str in line:
                count += 1
    except GeneratorExit:
        print("General Error")



@coroutine_decorator
def longer_than(n):
    count = 0
    try:
        while True:
            line = yield
            if len(line)>n:
                print(line)
                count += 1
    except GeneratorExit:
        print('longer than {}: {}'.format(n, count))

    c = match_counter('Da')

    sender('names.txt', c)

    l = longer_than(14)

    sender('names.txt', l)