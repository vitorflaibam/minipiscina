class HotBeverage:
    def __init__(self):
        self.name = "hot beverage"
        self.price = format(0.30,".2f")

    def description(self):
        return "description: Just some hot water in a cup."

class Coffee:
    def __init__(self):
        self.name = "coffee"
        self.price = format(0.40,".2f")

    def description(self):
        return "A coffee, to stay awake."

class Tea:
    def __init__(self) -> None:
        self.name = "tea"
        self.price = format(0.30,".2f")
        pass

    def description(self):
        return "Just some hot water in a cup."

class Chocolate:
    def __init__(self):
        self.name = "chocolate"
        self.price = format(0.50,".2f")
        pass

    def description(self):
        return "Chocolate, sweet chocolate..."

class Cappuccino:
    def __init__(self):
        self.name = "cappuccino"
        self.price = format(0.45,".2f")
        pass

    def description(self):
        return "Un po’ di Italia nella sua tazza!"

hot_beverage = HotBeverage()
coffee = Coffee()
tea = Tea()
chocolate = Chocolate()
cappuccino = Cappuccino()