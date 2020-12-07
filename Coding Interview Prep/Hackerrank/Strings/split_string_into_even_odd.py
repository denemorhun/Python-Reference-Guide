# split a string into even and odd indices

def split_string_into_even_odd(s):
    # have to use stride s[0:-1:2], start at 0, jump 2
    print(s[0::2], s[1::2])


def main():
   split_string_into_even_odd("Hacker")
   split_string_into_even_odd("Rank")

if __name__ == '__main__': main()
