#!/usr/bin/env python3
# author: Denem Orhun
'''
read entries from STDIN and return the list 
'''

# get the number of entries to be made       
def get_entries():
        # number of lines to be entered (t)
        print("Enter number of entries to be made")
        t = int(input())

        entries = []

        # read t lines from STDIN
        for i in range(0, t):
            entries.append(input().strip())
            print(entry[i])
        
        return entries

# print dictionary items where o is a dictionary
def print_dict(dic):
    for x in dic: print(f'{x}: {dic[x]}')

if __name__ == '__main__': main()
