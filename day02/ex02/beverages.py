class HotBeverage:
    def __init__(self):
        self.name = "hot beverage"
        self.price = 0.30


    def description(self):
        return "description: Just some hot water in a cup."

class Coffee:
    def __init__(self):
        self.name = "coffee"
        self.price = 0.40

    def description(self):
        return "A coffee, to stay awake."

class Tea:
    def __init__(self) -> None:
        self.name = "tea"
        self.price = 0.30
        pass

    def description(self):
        return "Just some hot water in a cup."

class Chocolate:
    def __init__(self):
        self.name = "chocolate"
        self.price = 0.50
        pass

    def description(self):
        return "Chocolate, sweet chocolate..."

class Cappuccino:
    def __init__(self):
        self.name = "cappuccino"
        self.price = 0.45
        pass

    def description(self):
        return "Un po’ di Italia nella sua tazza!"

hot_beverage = HotBeverage()
coffee = Coffee()
tea = Tea()
chocolate = Chocolate()
cappuccino = Cappuccino()

print("=-"*20)
print("name :", hot_beverage.name)
print("price :", hot_beverage.price) 
print("description :", hot_beverage.description())
print("=-"*20)
print("name :", coffee.name)
print("price :", coffee.price) 
print("description :", coffee.description())
print("=-"*20)
print("name :", tea.name)
print("price :", tea.price) 
print("description :", tea.description())
print("=-"*20)
print("name :", chocolate.name)
print("price :", chocolate.price) 
print("description :", chocolate.description())
print("=-"*20)
