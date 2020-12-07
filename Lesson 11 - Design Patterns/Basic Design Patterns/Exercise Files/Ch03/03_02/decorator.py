from functools import wraps
""" Add a blinker function to print with <blink> tags"""

def make_blink(function):
	"""Defines the decorator"""
	#This makes the decorator transparent in terms of its name and docstring

	@wraps(function)
	#Define the inner function
	def decorator():
		#Grab the return value of the function being decorated
		retval = function()
		retval = "<blink>" + retval + "</blink>"
		#Add new functionality to the function being decorated
		return retval

	# return wrapped function outcome	
	return decorator

def hello_world():
	"""Original function and not the decorator! """
	return "Hello, World!"

# first call the function without any decorator. 
print(hello_world())

# print with the decorator 
@make_blink
def hello_world_2():
	"""Modified function but not the decorator """
	return ("Hello, World!")

#Check the result of decorating
print(hello_world_2())

#Check if the function name is still the same name of the function being decorated
print(hello_world_2.__name__)

#Check if the docstring is still the same as that of the function being decorated
print(hello_world_2.__doc__)


