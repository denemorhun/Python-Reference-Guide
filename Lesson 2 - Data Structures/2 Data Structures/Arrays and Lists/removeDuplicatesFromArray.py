# remove duplicates

def removeDuplicates(l):
    l = sorted(set(l))
    return l

def main():
    l = [1,1,2,3,4,5, 1, 3, 7, 5, 3]
    print( removeDuplicates(l))

if __name__ == '__main__': main()