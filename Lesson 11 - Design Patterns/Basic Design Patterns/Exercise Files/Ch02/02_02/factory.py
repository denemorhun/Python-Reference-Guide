class Dog:
	"""A simple dog class"""

	def __init__(self, name):
		self._name = name

	def speak(self):
		return "Woof!"

class Cat:
	"""A simple cat class"""

	def __init__(self, name):
		self._name = name

	def speak(self):
		return "Meow!"


def get_pet (pet='dog'):
	"""The Factory Method"""
	pets = dict(dog=Dog("Hera"), cat=Cat("Minnos"))
	return pets[pet]

d = get_pet("dog")
print(d.speak())

c = get_pet("cat")
print(c.speak())

	