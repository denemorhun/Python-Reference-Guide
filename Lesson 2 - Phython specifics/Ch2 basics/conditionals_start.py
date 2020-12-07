#
# Example file for working with conditional statements
#

def main():
  x, y = 10, 100
  
  # conditional flow uses if, elif, else  

  if x < y:
    print("x is less than y")
  elif y < x: 
    print("ys is less than x")
  else:
      print("they are equal")

  # conditional statements let you use "a if C else b"
  print("x is greater" if x > y else "y is greater")

if __name__ == "__main__":
  main()
