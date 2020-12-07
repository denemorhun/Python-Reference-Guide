# Remove Dupes from sorted array

'''
given a dictionary, assuming keys and values are unique
swap keys and values
'''

def swapKeysValues(my_dict):
   
    if my_dict is None:
        return None

    # orig dict[k] -> v
    # dict[raptor] -> 3
    # new dict[v] -> k
    # dict[3] -> raptor
    new_dict = {}

    for k,v in my_dict.items():
        new_dict[v] = k

    return new_dict


if __name__ == '__main__':

    my_dict = {'raptor': 3, 'cat': 1, 'dog': 9, 'rabbit': 2}

    result = swapKeysValues(my_dict)

    print (f'new dict {result} ')