""" Creating and Combining Sets of Friends """

college = set(['Bill', 'Katy', 'Verne', 'Dillon',
               'Bruce', 'Olivia', 'Richard', 'Jim'])

coworker = set(['Aaron', 'Bill', 'Brandon', 'David',
                'Frank', 'Connie', 'Kyle', 'Olivia'])

coworker.add('Denem')
coworker.remove('Bill')

family = set(['Garry', 'Landon', 'Larry', 'Mark',
              'Olivia', 'Katy', 'Rae', 'Tom'])

# This is not supported for union
# all_friends2 = college + family + coworker
all_friends = college.union(coworker,family)
print("all my friends: ", *all_friends)

# people who appear in all groups
common_friends = college.intersection(coworker, family)
print("my common friends: ", *common_friends)
# olivia

# difference of coworkers who are not college buddies
prof_community = coworker - college
# same as above
prof_community = coworker.difference(college)
print(prof_community)

print(*coworker)

# create a temporary set
engagement = set(['Olivia'])
engagement.issubset(family)

# remove specific entry
engagement.discard('Olivia')
engagement.clear()

print(engagement)








