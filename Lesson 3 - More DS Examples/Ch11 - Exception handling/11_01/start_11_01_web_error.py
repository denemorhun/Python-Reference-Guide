""" Trying to Download Things That Don't Exist """

import urllib.request
try:
    webpage = urllib.request.urlopen('http://www.google.com')
except:
    print("When unable to connect to the internet")
# only when the try concludes, run the else. If not internet:
else:
    for line in webpage:
        print(line)
