#
# Example file for working with os.path module
#
import os
from os import path
import getpass
import datetime
from datetime import date, time, timedelta
import time


def main():
  # Print the name of the OS
  print(os.name)
  
  # Check for item existence and type, as long as the file is in the same directory
  # print ("Item exists: " + str(path.exists("myfile2.txt")))
  # print ("Item is a file: " + str(path.isfile("myfile2.txt")))
  # print ("Item is a directory: " + str(path.isdir("myfile2.txt")))
  # print ("Item is a directory: " + str(path.isdir("denem")))

  # print ("Basename is " + os.path.basename("/Users/dorhun/Desktop/Trainings/Python/textfile.txt"))
  # print ("Directory name is " + os.path.dirname("/Users/dorhun/Desktop/Trainings/Python/textfile.txt"))

  # # Work with file paths
  # print ("Item's path: " + str(path.realpath("textfile.txt")))

  # print ("Item's path and name: " + str(path.split(path.realpath("textfile.txt"))))

  
  #get ctime, printed in string
  # print ("time.ctime() : %s" % time.ctime())

  # Get the modification time
  t1 = time.ctime(path.getctime("myfile2.txt"))
  print(t1)

  print(datetime.datetime.fromtimestamp(path.getmtime("myfile2.txt")))
  # Calculate how long ago the item was modified

  td = datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime("myfile2.txt"))
  print("It has been ", td)

  # calculate total seconds
  print("and in seconds ", str(td.total_seconds ) + "seconds")

  # get the user logged in
  print("UID is", os.getuid(), " and user name is", getpass.getuser())
  
if __name__ == "__main__":
  main()
