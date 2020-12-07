#
# Example file for working with filesystem shell methods
#
import os
from os import path
import shutil
from shutil import make_archive
from zipfile import ZipFile

def main():
  # make a duplicate of an existing file
  if path.exists("myfile1.txt"):
    # get the path to the file in the current directory
    src = path.realpath("myfile1.txt")
    
    # # let's make a backup copy by appending "bak" to the name
    dst = src + ".bak"

    # now use the shell to make a copy of the file
    # shutil.copy(src, dst)
   
    # copy over the permissions, modification times, and other info
    shutil.copystat(src, dst)
    
   
    # rename the original file
    # orig = src + ".orig"
    # os.rename(path.realpath(src), orig)
   
    # now put things into a ZIP archive
    
    root_dir, tail = path.split(src)
    print ("root_dir", root_dir, "tail", tail)
    shutil.make_archive("archive", "zip", root_dir)

    # more fine-grained control over ZIP files
    with ZipFile("testzip.zip", "w") as newzip:
        newzip.write("myfile1.txt")
        newzip.write("myfile1.txt.bak")
 
      
if __name__ == "__main__":
  main()
