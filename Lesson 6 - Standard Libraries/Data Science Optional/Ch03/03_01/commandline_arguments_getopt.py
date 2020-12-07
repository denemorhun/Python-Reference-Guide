#!/usr/bin/python3
# Command Line Arguments
import sys, getopt

def main():

    # Remove script name from list of args
    sys.argv.remove(sys.argv[0])

    # pick uption
    arguments = sys.argv
   
    try:
        opts, args = getopt.getopt(arguments,"loc:people")
        #opts, arguments = getopt.getopt(arguments,"pass:loc:people",["lat","long"])
    except getopt.GetoptError:
        print ('Please conform to the syntax: test.py -pass -loc <lat><long> -people')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ('test.py -pass -loc <lat><long> -people')
            sys.exit()
        # if opt in ("-pass", "--lat", "--long"):
        #     print("Calling position function")
        if opt == '-loc':
            print("calling location function")
        if opt == "-people":
            print("Calling people function")

if __name__ == "__main__": main()