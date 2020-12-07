# 
# Example file for retrieving data from the internet
#

import urllib.request

def main():
  webUrl = urllib.request.urlopen("http://www.google.com")

  # open url: 200 if we can connect
  print("Result code", str(webUrl.getcode()))

  # print the url
  print(str(webUrl.geturl()))

  print(str(webUrl.getheaders()))

  # read some data (html code for google's homepage)
  data = webUrl.read()
  print(data)


if __name__ == "__main__":
  main()
