class SubsystemA:

	def method1(self):
		print('SubsystemA method1 ...')
		
	def method2(self):
		print('SubsystemA method2 ...')

class SubsystemB:
	
	def method1(self):
		print('SubsystemB method1 ...')
		
	def method2(self):
		print('SubsystemB method2 ...')

class Facade:

	def __init__(self):
		self._SubsystemA = SubsystemA()
		self._SubsystemB = SubsystemB()

	def method(self):
		self._SubsystemA.method1()
		self._SubsystemA.method2()

		self._SubsystemB.method1()
		self._SubsystemB.method2()
				

def main():
	f = Facade()
	f.method()
	

if __name__ == "__main__":
	main()
