""" The Hierarchy of Packages and finding them in python"""

import urllib.request

# retrieve google.com home page
print(urllib.request.urlopen('http://www.google.com'))

# get the path to urllib package
print(urllib.__path__)

# very useful: /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/urllib']


