# function solution
def even_integers_function(n):
    result = [i for i in range(n) if i%2 == 0]
    return result

print(even_integers_function(10))