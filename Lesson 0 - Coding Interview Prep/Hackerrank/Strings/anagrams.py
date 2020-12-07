''' Find all given anagrams

# sort every string alphabetically and store in a dictionary
# compare each word from the input to the dictionary
# if the word is already in the dictionary, append its value to the key
 '''


def find_anagrams(words):

    # initialize a dictionary to store sorted anagrams
    reference = {}

    for word in words:
        # sort every string alphabetically and convert to string
        sorted_word ="".join(sorted(word))

        #check if key is in dictionary
        if sorted_word in reference.keys():
            # append the original word to the key
            reference[sorted_word].append(word)
        else:
            #if no sorted match is found, return None
            reference[sorted_word] = [word]

    return list(reference.values())

def main():
    words = ["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp", "tca", "bbb", "bbb"]

    print(find_anagrams(words))

if __name__ == '__main__': main()
