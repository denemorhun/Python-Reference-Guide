# check if a string consists of unique characters using sets

def check_if_unique(input):

    return "unique" if len(input) == len(set(input)) else "not unique"

def main():
   print( check_if_unique("iyi geceler ege"))
   print(check_if_unique("seda"))
   print(check_if_unique("AAA"))

if __name__ == '__main__': main()
