class Korean:
	"""Korean speaker"""
	def __init__(self):
		self.name = "Korean"

	def speak_korean(self):
		return "An-neyong?"

class British:
	"""English speaker"""
	def __init__(self):
		self.name = "British"	

	#Note the different method name here!
	def speak_english(self):
		return "Hello!"	

class Turkish:
	""" Turkish speaker"""
	def __init__(self):
		self.name = "Turkish"

	def speak_turkish(self):
		return "selam"

class Adapter:
	"""This changes the generic method name to individualized method names"""

	def __init__(self, object, **adapted_method):
		"""Change the name of the method"""
		self._object = object

		#Add a new dictionary item that establishes the mapping between the generic method name: speak() and the concrete method
		#For example, speak() will be translated to speak_korean() if the mapping says so
		self.__dict__.update(adapted_method)

	def __getattr__(self, attr):
		"""Simply return the rest of attributes!"""
		return getattr(self._object, attr)
		
#List to store speaker objects
speaker_objects = []

#Create a Korean object
korean = Korean()

#Create a British object
british =British()

#create a Turkish object 

turkish = Turkish()

#Append the objects to the objects list
speaker_objects.append(Adapter(korean, speak=korean.speak_korean))
speaker_objects.append(Adapter(british, speak=british.speak_english))
speaker_objects.append(Adapter(turkish, speak=turkish.speak_turkish))

# print all the speak objects in dict and make them speak
for obj in speaker_objects:
	print(f"{obj.name} says '{obj.speak()}'\n")

