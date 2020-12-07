''' Swap variables using short hand '''

def swap_variables(a, b) -> bool:

    a, b = b, a

    return [a, b]

def main():
    print(swap_variables(3, 5))

if __name__ == '__main__': main()
