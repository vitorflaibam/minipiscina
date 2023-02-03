import sys

def statess():
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
        estado = statess()
        # estado.get(inpu t)# recebe estado e retorna o valor dela (sigla)
        result = capital_cities()
        final = result.get(estado.get(input)) # recebe a sigla e retorna o valor dela (capital)
        if input in estado.keys():
            print(final)
        else: sys.exit("Unknown state.")

if __name__ == '__main__':
    getstate()
