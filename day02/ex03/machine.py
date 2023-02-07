import random
import beverages

class CoffeeMachine:
    def __init__(self) -> None:
        pass

    class EmptyCup(beverages.HotBeverage):
        def __init__(self, price, name, description):
            super().__init__(price, name, description)

    class BrokenMachineException(Exception):
        def __init__(self, *args: object) -> None:
            super().__init__("This coffee machine has to be repaired.")

    def repair(self):
        self.counter=0
        
    def serve(self, beverage):
        self.beverage = beverages.HotBeverage
        raise(Exception (CoffeeMachine.BrokenMachineException))
        return EmptyCup