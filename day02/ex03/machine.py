import random
from beverages import *

class CoffeeMachine:
    def __init__(self) -> None:
        ...

    class EmptyCup(HotBeverage):
        def __init__(self, name="empty cup", price=0.90):
            super().__init__(price, name)
        
        def description(self):
            return "An empty cup?! Gimme my money back!"

    class BrokenMachineException(Exception):
        def __init__(self) -> None:
            super().__init__("This coffee machine has to be repaired.")

    def repair(self):
        self.counter=0
        
    def serve(self, beverage):
        self.beverage = HotBeverage
        random.choice(beverage)
        raise(CoffeeMachine.BrokenMachineException)
        if serve() > 10:
            repair()
        return EmptyCup