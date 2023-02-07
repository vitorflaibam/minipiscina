class HotBeverage:
    def __init__(self):
        self.name = "hot beverage"
        self.price = 0.30

    def description(self):
        return "Just some hot water in a cup."

    def __str__(self) -> str:
        params= "name : " + self.name + "\nprice : " + format(self.price,".2f") + "\ndescription : " + self.description()
        return params

class Coffee:
    def __init__(self):
        self.name = "coffee"
        self.price = 0.40

    def description(self):
        return "A coffee, to stay awake."

    def __str__(self) -> str:
        params= "name : " + self.name + "\nprice : " + format(self.price,".2f") + "\ndescription : " + self.description()
        return params

class Tea:
    def __init__(self) -> None:
        self.name = "tea"
        self.price = 0.30
        pass

    def description(self):
        return "Just some hot water in a cup."

    def __str__(self) -> str:
        params= "name : " + self.name + "\nprice : " + format(self.price,".2f") + "\ndescription : " + self.description()
        return params

class Chocolate:
    def __init__(self):
        self.name = "chocolate"
        self.price = 0.50
        pass

    def description(self):
        return "Chocolate, sweet chocolate..."

    def __str__(self) -> str:
        params= "name : " + self.name + "\nprice : " + format(self.price,".2f") + "\ndescription : " + self.description()
        return params

class Cappuccino:
    def __init__(self):
        self.name = "cappuccino"
        self.price = 0.45
        pass

    def description(self):
        return "Un po’ di Italia nella sua tazza!"

    def __str__(self) -> str:
        params= "name : " + self.name + "\nprice : " + format(self.price,".2f") + "\ndescription : " + self.description()
        return params

hot_beverage = HotBeverage()
coffee = Coffee()
tea = Tea()
chocolate = Chocolate()
cappuccino = Cappuccino()

print("-"*50)
print(hot_beverage)
print("-"*50)
print(coffee)
print("-"*50)
print(tea)
print("-"*50)
print(chocolate)
print("-"*50)
print(cappuccino)
print("-"*50)