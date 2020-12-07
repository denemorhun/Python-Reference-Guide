#The house class being visited 
class House(object): 
	def accept(self, visitor):
		"""Interface to accept a visitor"""
		#Triggers the visiting operation, self is the house object
		visitor.visit(self)

	# method to work on the ac
	def work_on_hvac(self, hvac_specialist):
		#Note that we now have a reference to the HVAC specialist object in the house object!
		print(self, "worked on by", hvac_specialist)

	# method to work on electricity
	def work_on_electricity(self, electrician):
		#Note that we now have a reference to the electrician object in the house object!
		print(self,"worked on by", electrician )

	def __str__(self):
		"""Simply return the class name when the House object is printed"""
		return self.__class__.__name__


class Visitor(object):
	"""Abstract visitor"""

	def __init__(self, name=""):
		self.name = name #Set the name of the visitor

	def __str__(self):
		"""Simply return the class name when the Visitor object is printed"""
		return self.__class__.__name__
	# we don't have an abstract visit method defined here


class HvacSpecialist(Visitor): 
	#Inherits from the parent class, Visitor
	"""Concrete visitor: HVAC specialist"""
	def visit(self, house):
		#Note that the visitor now has a reference to the house object
		house.work_on_hvac(self) 


class Electrician(Visitor): 
	#Inherits from the parent class, Visitor
	"""Concrete visitor: electrician"""
	def visit(self, house):
		house.work_on_electricity(self)
		#Note that the visitor now has a reference to the house object

#Create an HVAC specialist
hvac = HvacSpecialist("ali")

#Create an electrician
elec = Electrician("Hakan")

#Create a house
dikili = House()
print(dikili)


#Let the house accept the HVAC specialist and work on the house by invoking the visit() method
hvac.visit(dikili)
dikili.accept(hvac)
dikili.work_on_hvac(hvac)


#Let the house accept the electrician and work on the house by invoking the visit() method
elec.visit(dikili)
dikili.accept(elec)
dikili.work_on_electricity(elec)


