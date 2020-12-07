def count_to(count):
	"""Our iterator implementation"""
	
	#Our list
	numbers_in_german = ["eins", "zwei", "drei", "vier", "funf"]


	#Creates a tuple such as (1, "eins")
	iterator = enumerate(numbers_in_german, 1)
	
	#Iterate through our iterable list
	#Extract the German numbers
	#Put them in a generator called number
	for position, number in iterator:
		if (position <= count):
			print(number)
		else:
			break
		#Returns a 'generator' containing numbers in German
		
#Let's test the generator returned by our iterator

count_to(5)
	