""" You Can Change an Outfit, But You Can't Change Your Words """

# create a closet full of clothes
closet = ['shirt','hat','pants','jacket','socks']
print(*closet)

closet.append('skirt')

# remove a hat
closet.remove('hat')
print(closet)
print(id(closet))

closet_orig = closet.copy()
if closet_orig is not closet:
    closet.clear()

print("The length of the closet", len(closet_orig))

print("Closet is now", *closet)

# create a poor choice of words
words = "You're wearing that"
print(words)
print(id(words))

# add more to the phrase
words = words + ' because you look great!'
print(words)
print(id(words))
