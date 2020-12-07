"""Organize files within a directory"""
import os, sys
from pathlib import Path

pwd = os.path.join(sys.path[0]) + '/'

SUBDIRECTORIES = {
    "DOCUMENTS": ['.pdf','.rtf','.txt'],
    "AUDIO": ['.m4a','.m4b','.mp3'],
    "VIDEOS": ['.mov','.avi','.mp4'],
    "IMAGES": ['.jpg','.jpeg','.png']
}

def pickDirectory(value):
    for category, suffixes in SUBDIRECTORIES.items():
        for suffix in suffixes:
            if suffix == value:
                return category
    # if file type doesn't exist
    return 'MISC'

def organizeDirectory():
    for item in os.scandir(pwd):

        if item.is_dir():
            continue

        filePath = Path(item)
   
        # create fileType
        fileType = filePath.suffix.lower()
        # return a directory type to place the file in
        directory = pickDirectory(fileType)
        directoryPath = Path(pwd + directory)

        if not directoryPath.is_dir():
            directoryPath.mkdir()

        filePath.rename(directoryPath.joinpath(filePath))

# call the function
organizeDirectory()