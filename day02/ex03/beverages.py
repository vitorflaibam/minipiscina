class HotBeverage:
	def __init__(self, name="hot beverage", price=0.30):
		self.name = name
		self.price = price

	def description(self):
		return "Just some hot water in a cup."

	def __str__(self) -> str:
		params= "name : " + self.name + "\nprice : " + format(self.price,".2f") + "\ndescription : " + self.description()
		return params

class Coffee(HotBeverage):
	def __init__(self):
		super().__init__(name="coffee", price=0.40)

	def description(self):
		return "A coffee, to stay awake."

class Tea(HotBeverage):
	def __init__(self) -> None:
		super().__init__(name="tea", price=0.30)

	def description(self):
		return "Just some hot water in a cup."

class Chocolate(HotBeverage):
	def __init__(self):
		super().__init__(name="chocolate", price=0.50)

	def description(self):
		return "Chocolate, sweet chocolate..."

class Cappuccino(HotBeverage):
	def __init__(self):
		super().__init__(name="cappuccino", price=0.45)

	def description(self):
		return "Un po’ di Italia nella sua tazza!"
