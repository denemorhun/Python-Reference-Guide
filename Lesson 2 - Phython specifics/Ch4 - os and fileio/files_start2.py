# file_start2.py

# Python program to illustrate
# Append vs write mode

from datetime import date

today = date.today()
tomorrow = date(year=today.year, month=today.month, day=today.day+1 )


file1 = open("myfile2.txt", "w") 
L = ["This is Izmir \n", "This is Paris \n", "This is London"] 
file1.writelines(L) 
file1.close() 
   
# Append-adds at last 
file1 = open("myfile2.txt", "a")  # append mode 
file1.write("\n\rToday is " + today.strftime("%D %A %B %Y")) 
file1.close() 
   
file1 = open("myfile2.txt", "r") 
print("Output of Readlines after appending") 
print(file1.read()) 
print() 
file1.close() 
   
# Write-Overwrites 
file1 = open("myfile2.txt", "w")  # write mode 
file1.write("Tomorrow will be " + tomorrow.strftime("%D %A %B %Y")) 
file1.close() 
   
file1 = open("myfile2.txt", "r") 
print("Output of Readlines after writing") 
print(file1.read()) 
print() 
file1.close() 