# hardcoded location
# filepath = '/Users/dorhun/Desktop/Trainings/Python/Automation/Python_Automation/Exercise Files/File IO/'

import os, sys

filepath = os.path.join(sys.path[0]) + '/'

passedFile = open(filepath + "peopleWhoPassed.txt", 'w')
failedfile = open(filepath + "peopleWhoFailed.txt", 'w')


with open(f'{filepath}inputFile.txt', 'r') as f:
    # print(f.read())
    for line in f:
        line_split = line.split()
        if line_split[2] == 'P':
            passedFile.write(line)
        elif line_split[2] == 'F':
            failedfile.write(line)

f.close()
passedFile.close()
failedfile.close()