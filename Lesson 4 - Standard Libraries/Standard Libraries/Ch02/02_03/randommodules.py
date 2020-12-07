# Random Module
import random as r
# Random Numbers
print(r.random())

decider = r.randrange(2)

if decider == 0:
    print('heads')
else:
    print('tails')
# Random Choices - using sample

# should print 5 from a range of 100
print("Sample of 5 nums " + str(r.sample(range(100),5)))

# Using choice to randomly select a pet
possiblePets = ["cat", "dog", "fish"]

print(r.choice(possiblePets))

# using shuffle to unsort a list (not tuple)

cards = ['J','Q','K','A']
r.shuffle(cards)

print(cards)