# Itertools Part 2
import itertools

# Permutations: Order matters - some copies with same inputs but in different order
election = {1: "barb", 2:"Karen", 3:"Erin"}

for p in itertools.permutations(election.values()):
    print(p)

# Combinations: Order does not matter - no copies with same inputs

colors_for_painting = ["Red", "Blue", "Purple", "Orange", "Yellow", "Pink"]

for c in itertools.combinations(colors_for_painting,2):
    print(c)