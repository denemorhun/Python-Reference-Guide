"""Abstract class Command"""
class Command:
	def execute(self):
		pass

"""Copy extends command"""
class Copy(Command):
	def execute(self):
		print("Copying")

"""Paste extends command"""
class Paste(Command):
	def execute(self):
		print("Pasting ...")

"""Save extends command"""
class Save(Command):
	def execute(self):
		print("Saving ...")

"""Execute all"""
class Macro:
	def __init__(self):
		self.commands = []

	def add(self, command):
		self.commands.append(command)

	def run(self):
		for c in self.commands:
			c.execute()
		
def main():
	my_macro = Macro()
	my_macro.add(Paste())
	my_macro.add(Save())
	my_macro.add(Copy())
	
	my_macro.run()

if __name__ == "__main__":
	main()
