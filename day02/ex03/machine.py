import random
from beverages import *

class CoffeeMachine:
	def __init__(self) -> None:
		self.counter = 0

	class EmptyCup(HotBeverage):
		def __init__(self, name="empty cup", price=0.90):
			super().__init__(name, price)
		
		def description(self):
			return "An empty cup?! Gimme my money back!"

	class BrokenMachineException(Exception):
		def __init__(self) -> None:
			super().__init__("This coffee machine has to be repaired.")

	def repair(self):
		print("This machine was repaired.")
		self.counter=0
	 
	def serve(self, beverage):
		choices = [CoffeeMachine.EmptyCup(), beverage()]
		if self.counter <= 10:
			self.counter += 1
			return(random.choice(choices))
		else:
			raise(CoffeeMachine.BrokenMachineException)

if __name__ == "__main__":
	machine = CoffeeMachine()
	choices = [Tea, Chocolate, Cappuccino, HotBeverage, Coffee]
	try:
		for i in range(20):
			print(machine.serve(random.choice(choices)))
	except Exception as e:
		print(e)
		machine.repair()
	try:
		for i in range(20):
			print(machine.serve(random.choice(choices)))
	except Exception as e:
		print(e)