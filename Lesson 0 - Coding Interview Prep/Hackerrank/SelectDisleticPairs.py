import random

def selectDysleticLetters():
    dysleticPairs = [('m','w'),('w','m'),('u','n'),('n','u'),('d','b'),('b','d'),('z','s'),('s','z'),('p','q'),('q','p'),('h','y'),('y','h')]
    # future pairs would include 2 5, 6 9

    alphabet = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')

    # your code increments the number of characters to be added, instead of the full_alphabet
    combinedChars = random.choice(dysleticPairs) + alphabet

    # avoid duplicates from list using list comprehension
    displayedChars = [] 
    [displayedChars.append(x) for x in combinedChars if x not in displayedChars] 

    return displayedChars
  
output = selectDysleticLetters()

# letter to find should be the first on the displayed list, before list is shuffled
letterToFind = output[0]

random.shuffle(output)

print ("The list of letters : ")
print(output)

# this is where your code should get the letter to search for
print('Find the letter: ' + letterToFind)

