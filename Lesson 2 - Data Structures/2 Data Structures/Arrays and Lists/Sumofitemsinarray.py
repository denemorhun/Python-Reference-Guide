# sum of items in array and list comphrension

# *result*  = [*transform*    *iteration*         *filter*     ]
#create new squares list using comphrehension
new_list = [i*i for i in range(10)]
print (new_list)

print("print contents of list")
for i in new_list:
    print(i)

print("print the sum of items")
print(sum(new_list))

