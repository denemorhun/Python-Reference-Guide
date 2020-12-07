#!/usr/bin/python3
# Command Line Arguments
import argparse

def loc():
    print("Calling location")

def people():
    print("Calling People")

def nextpass(lat, long):
    print(f'Calling pass, lat {lat}, long {long}')

def run_parse():
    # create a parser
    parser = argparse.ArgumentParser(description='Return info about the ISS.')

    #next pass
    parser.add_argument('-n','--nextpass', required=False, metavar='l', type=int, nargs=2,
                        help='Position of the ISS, input lat, long')



    # parser.add_argument('--sum', dest='accumulate', required=False, action='store_const',
    #                     const=sum, default=max,
    #                     help='sum the integers (default: find the max)')
    parser.add_argument('-p','--people', required=False, action='store_true',
                        help='display the people on board the craft')
    parser.add_argument('-l', '--location', action='store_true', required=False, help='display the current ISS location')


    args = parser.parse_args()
    # print(args.accumulate(args.integers))
    print(args)

    if args.location == True:
        loc()

    if args.people == True:
        people()

    if args.nextpass != None:
        nextpass( args.nextpass[0], args.nextpass[1] )



def main():
    run_parse()

if __name__ == "__main__": main()