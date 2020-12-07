
def coroutine_example():
    while True:
        x = yield
        #do something with x
        print (x)

c = coroutine_example()

#prime the coroutine

next(c)

c.send(10)
