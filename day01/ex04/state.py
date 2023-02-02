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

def chave_capital(val):
    for chavecapital, value in capital_cities.items():
        if val == value:
            return chavecapital
    
def chave_estado(val):
    for chavestado, value in states.items():
        if val == value:
            return chavestado
    return None

def rodar():
    if len(sys.argv) != 2:
        sys.exit(0)
    else:
        input = sys.argv[1]
        chave_capitaltest = chave_capital(input)
        chavestado = chave_estado(chave_capitaltest)
        if chavestado != None: 
            print(chavestado)
        else:
            print("Unknown state.")

if __name__ == '__main__':
    rodar()
