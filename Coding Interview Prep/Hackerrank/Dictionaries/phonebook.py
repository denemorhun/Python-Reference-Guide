#!/usr/bin/env python3
# author: Denem Orhun
'''
Task
    Given names and phone numbers, assemble a phone book that maps 
    friends' names to their respective phone numbers. You will then be 
    given an unknown number of names to query your phone book for. For each
     queried, print the associated entry from your phone book on a new line in 
     the form name=phoneNumber; if an entry for  is not found, print Not found instead.

    Note: Your phone book should be a Dictionary/Map/HashMap data structure.

Input Format

    The first line contains an integer,n,  denoting the number
    of entries in the phone book.
    Each of the  subsequent lines describes an entry in the form of
    space-separated values on a single line. The first value is a
    friend's name, and the second value is an -digit phone number.

    After the lines of phone book entries, there are an unknown
    number of lines of queries. Each line (query) contains a  to look up
    and you must continue reading lines until there is no more input.

    Note: Names consist of lowercase English alphabetic letters and are first names only.

    Constraints

    Output Format

    On a new line for each query, print Not found if the name has
    no corresponding entry in the phone book; otherwise, print the full and
    in the format name=phoneNumber.

    Sample Input

    3
    sam 99912222
    tom 11122222
    harry 12299933
    sam
    edward
    harry
    Sample Output

    sam=99912222
    Not found
    harry=12299933
'''

def main():
    # phonebook = {'sam':99912222, 'tom': 11122222, 'harry':12299933 }

    entries = read_entries()
    
    # use a comphrension to convert list into dictionary
    phone_book = dict(entry.split(" ") for entry in entries)

    while True:
        try:
            print("Enter name: ")
            name = input()
            if name == "":
                break
            if name in phone_book.keys():
                print(f'{name}={phone_book[name]}')
            else:
                print("Not found")
        except EOFError:
            break 
    

   # print_dict(phone_book)

# get the number of entries to be made       
def read_entries():
        # number of lines to be entered (t)
        print("Enter number of entries to be made")
        t = int(input())

        entries = []

        # read t lines from STDIN
        for i in range(0, t):
            entries.append(input().strip())
        
        return entries



# print dictionary items where o is a dictionary
def print_dict(dic):
    for x in dic: print(f'{x}={dic[x]}')

if __name__ == '__main__': main()
