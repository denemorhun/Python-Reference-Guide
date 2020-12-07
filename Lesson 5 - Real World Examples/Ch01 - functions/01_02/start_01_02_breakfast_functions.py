""" A Functional Breakfast """

def cook_and_mix():
    print('Mixing the ingredients')
    print('Pouring the mixture into a frying pan')
    print('Cooking the first side')
    print('Flipping it!')
    print('Cooking the other side')

def make_crepe():
    cook_and_mix()
    crepe = 'a tasty crepe'
    return crepe

def make_omelette(*ingredient):
    cook_and_mix()
    omelette = 'a tasty {} omelette'.format(ingredient)
    return omelette

def make_pancake():
    cook_and_mix()
    pancake = 'a delicious pancake'
    return pancake

om1 = make_omelette(' cheese ', 'mushroom', 'onion')
pan1 = make_pancake() + " 1"
om2 = make_omelette(' mushroom ') 

crep1 = make_crepe() + " 1"

print(om1)
print(pan1)
print(om2)
print(crep1)