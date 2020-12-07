#
# Read and write files using the built-in Python file methods
#

import os
import sys


def main():

    # Open file in the same location as the script reliably
    # with open(os.path.join(sys.path[0], "textfile.txt"), "w+") as f:
    #     for i in range(10):
    #         f.write("This is line number " + str(i) + "\r\n")

    # Open a file for writing and create it if it doesn't exist
    # f = open("textfile.txt","w+")
    # Open the file for appending text to the end
    f = open("textfile.txt","w+")
    
    # write some lines of data to the file
    for i in range(10):
        f.write("This is line %d\r\n" % (i+1))

    f.close()

    # Open the file for appending text to the end
    # with open(os.path.join(sys.path[0], "textfile.txt"), "r") as f:
    #     f.write("This is line number XXXX")

    # f = open("textfile.txt", "a")
    # f.write("This is line number XXXX")
    

    # write some lines of data to the file
    # for i in range(10):
        # f.write("This is line number " + str(i) + "\r\n")

    # close the file when done
    #f.close()

    # Open the file back up and read the contents
    # with open(os.path.join(sys.path[0], "textfile.txt"), "r") as f:
       
    f = open("textfile.txt","r")
    if f.mode == 'r': # check to make sure that the file was opened
    # use the read() function to read the entire file
        contents = f.read()
    print (contents)


    if __name__ == "__main__":
        main()
