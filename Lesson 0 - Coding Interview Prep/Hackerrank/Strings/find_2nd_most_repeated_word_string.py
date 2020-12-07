'''

Given a sequence of strings, the task is to find out the second most repeated (or frequent) string in the given sequence.(Considering no two words are the second most repeated, there will be always a single word).

Examples:

Input : {"aaa", "bbb", "ccc", "bbb", 
         "aaa", "aaa"}
Output : bbb

Input : {"geeks", "for", "geeks", "for", 
          "geeks", "aaa"}
Output : for
Asked in : Amazon


# import Counter from collections
# split given string separated by space
# Convert the list of words into dictionary using Counter
# strings will be become keys and frequency values
# traverse again and print if frequency > 1
'''

from collections import Counter

def find_2nd_most_repeated(words):

    # split given string separated by space
    words = words.split(" ")
 
    # Convert the list of words into dictionary using Counter
    word_frequency = Counter(words)

    # print out the frequencies
    for key, value in word_frequency.items():
        print(key, value)

    # get max value from the occurrences
    max_value = max(word_frequency.values())
    max2 = 0

    # traverse the dictionary and if curr_value is more than max2
    # and other than the maximum value set max2 as curr_value
    for curr_value in word_frequency.values():
        if curr_value < max_value and curr_value > max2:
            max2 = curr_value

    # Reverse the keys and values, assuming frequencies are unique. 
    for key, value in word_frequency.items(): 
         if max2 == value: 
             return key 


def main():
    inputString = ("aaa bbb cccc aaa bbb aaa ddd")

    print("Second most repeated string", find_2nd_most_repeated(inputString))

if __name__ == '__main__': main()
