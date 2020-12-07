#!/usr/bin/python3
# Command Line Arguments
import argparse

# create a parser
parser = argparse.ArgumentParser(description='Process some integers.')
#next pass
parser.add_argument('-d','--pas', required=False, metavar='l', type=int, nargs=2,
                    help='Position of the ISS, input lat, long')


# parser.add_argument('--sum', dest='accumulate', required=False, action='store_const',
#                     const=sum, default=max,
#                     help='sum the integers (default: find the max)')
parser.add_argument('-c','--people', required=False,
                    help='display the people on board the craft')
parser.add_argument('-loc', '--location', required=False, 
                    help='display the current ISS location')



args = parser.parse_args()
# print(args.accumulate(args.integers))
print(args)

# def main():
#     choose_option()

# if __name__ == "__main__": main()