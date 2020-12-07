# function solution
def even_integers_function(n):
    result = [i for i in range(n) if i%2 == 0]
    return result

print(even_integers_function(10))

def test_func():
    print(sum(even_integers_function(10)))
    assert sum(even_integers_function(10)) == 20
    print(sum(even_integers_function(0)))
    assert sum(even_integers_function(0)) == 0