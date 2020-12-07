# Demonstrate the usage of defaultdict objects

from collections import defaultdict

def main():
    # define a list of items that we want to count
    fruits = ['apple', 'pear', 'orange', 'banana',
              'apple', 'grape', 'banana', 'banana']

    # use a dictionary to count each element

    # we can initialize it
    # fruitCounter = {'apple':0, 'pear':0, 'orange':0,'banana':0,'grape':0}


    # we can use normal dicts
    # fruitCounter = {}
    # # Count the elements in the list
    # for fruit in fruits:
    #     if fruit in fruitCounter.keys()
    #         fruitCounter[fruit] += 1
    #     else:
    #         fruitCounter[fruit] = 1


    # we can use a defaultDict, starting with a lambda count of 10
    fruitCounter = defaultdict(lambda: 10)
    # Count the elements in the list

    # print the result
    for fruit in fruits:
        fruitCounter[fruit] += 1

    for k,v in fruitCounter.items():
        print(f"Fruit {k}:  {v} occurence(s)")
    """
    Fruit apple:  12 occurence(s)
    Fruit pear:  11 occurence(s)
    Fruit orange:  11 occurence(s)
    Fruit banana:  13 occurence(s)
    Fruit grape:  11 occurence(s)  
    """

if __name__ == "__main__":
    main()
