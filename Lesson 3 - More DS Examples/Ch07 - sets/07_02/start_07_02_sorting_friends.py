""" Sorting Friends into Sets """

# set of all friends
friends = set(['Mark', 'Rae', 'Verne', 'Richard',
               'Aaron', 'David', 'Bruce', 'Garry',
               'Bill', 'Connie', 'Larry', 'Jim',
               'Landon', 'Dillon', 'Frank', 'Tom',
               'Kyle', 'Katy', 'Olivia', 'Brandon'])

# set of people who live in my zip code
zipcode = set(['Jerry', 'Elaine', 'Cindy', 'Verne',
                'Rudolph', 'Bill', 'Olivia', 'Jim',
                'Lindsay', 'Rae', 'Mark', 'Kramer',
                'Landon', 'Newman', 'George'])

# set of people who play Munchkin
munchkins = set(['Steve', 'Jackson', 'Frank', 'Bill',
                 'Mark', 'Landon', 'Rae'])

# set of Olivia's friends
olivia = set(['Jim', 'Amanda', 'Verne', 'Nestor'])

# take the subset of friends who live close
invite = friends.intersection(zipcode)
# remove people who are already playing a game
invite = invite - munchkins

#merge with Olivia's friends
olivia_available = olivia
# Nestor is in Romania
olivia_available.discard('Nestor')
invite = invite.union(olivia_available)

print(invite)
        
while len(invite) > 0:
    f = invite.pop()
    if f is not 'Olivia':
        print(f"Call {f} and invite over!")

# we can also do this using for
# for buddy in invite:
    #    if f is not 'Olivia':
    #    print(f"Call {f} and invite over!")

    