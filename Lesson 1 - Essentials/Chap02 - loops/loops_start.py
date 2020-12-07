#
# Example file for working with loops
#

def main():
  x = 0

  # define a while loop
  while (x < 5):
    x += 1
    print(x)

  # define a for loop
  for x in range(6, 11):
    print(x)
   
  # use a for loop over a collection
  items = {'apple','banana','pineapple'}
  for i in items:
    print(i)
    
  # use the break and continue statements

  # define a for loop with break
  print("define a for loop with break")
  for x in range(12, 16):
    if x == 13: break
    # if x is 13, break loop
    print(x)
    
  # define a while loop with continue
  print("define a while loop with continue")
  for x in range(20, 25):
    # if divisible by 2 skip those
    if x % 2 == 0: continue
    print(x)

  #using the enumerate() function to get index 
  days = ["Mon","Wed","Fri"]
  for i,d in enumerate(days):
    print(i+1, d)

if __name__ == "__main__":
  main()
