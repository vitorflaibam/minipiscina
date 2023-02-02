import sys

def states():
    states = {
    "Oregon" : "OR",
    "Alabama" : "AL",
    "New Jersey": "NJ",
    "Colorado" : "CO"
    }
    return states

def capital_cities():
    capital_cities = {
    "OR": "Salem",
    "AL": "Montgomery",
    "NJ": "Trenton",
    "CO": "Denver"
    }
    return capital_cities

def getstate():
    if len(sys.argv) != 2:
        sys.exit(0)
    else: 
        input = sys.argv[1]
        estado = states.get(input) # recebe estado e retorna o valor dela (sigla)
        result = capital_cities.get(estado) #recebe a sigla e retorna o valor dela (capital)
        if input in states.keys():
            print(result)
        else: sys.exit("Unknown state.")

if __name__ == '__main__':
    getstate()
