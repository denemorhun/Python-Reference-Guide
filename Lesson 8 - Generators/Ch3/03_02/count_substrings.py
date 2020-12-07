
# Determine if input is a string
# increment counter for substrings sent that much initial string

def count_substrings(string):
    count = 0
    try:
        while True:
            item = yield
            if isinstance(item, str):
                if item in string:
                    count += 1
                    print(item)
                else:
                    print('No Match')
            else:
                print('Not a string')
    except GeneratorExit:
        print(count)


c = count_substrings('denem')
next(c)

c.send('ene')
# 1
c.send('e')
# 2
c.send('nn')
# No Match

c.send(123)
# not a string

c.close()