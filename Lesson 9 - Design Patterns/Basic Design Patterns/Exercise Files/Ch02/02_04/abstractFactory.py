class Dog:
	"""One of the objects to be returned"""

	def speak(self):
		return "Woof!"

	def __str__(self):
		return "Dog"


class DogFactory:
	"""Concrete Factory"""

	def get_pet(self):
		"""Returns a Dog object"""
		return Dog()

	def get_food(self):
		"""Returns a Dog Food object"""
		return "Dog Food!"

class Cat:
	"""One of the objects to be returned"""

	def speak(self):
		return "Meow!"

	def __str__(self):
		return "Cat"


class CatFactory:
	"""Concrete Factory"""

	def get_pet(self):
		"""Returns a Dog object"""
		return Cat()

	def get_food(self):
		"""Returns a Cat Food object"""
		return "Cat Food!"



class PetStore:
	""" PetStore houses our Abstract Factory """

	def __init__(self, pet_factory=None):
		""" pet_factory is our Abstract Factory """

		self._pet_factory = pet_factory


	def show_pet(self):
		""" Utility method to display the details of the objects retured by the Factory """

		pet = self._pet_factory.get_pet()
		pet_food = self._pet_factory.get_food()

		print("Our pet is '{}'!".format(pet))
		print("Our pet says hello by '{}'".format(pet.speak()))
		print("Its food is '{}'!".format(pet_food))

#Create a Concrete Factory
dog_factory = DogFactory()

#Create a pet store housing our Abstract Factory
dog_shop = PetStore(dog_factory)

#Invoke the utility method to show the details of our pet, which in our case is the dog
dog_shop.show_pet()

cat_factory = CatFactory()
cat_shop = PetStore(cat_factory)
cat_shop.show_pet()