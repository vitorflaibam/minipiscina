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
    capitals = capital_cities()
    for chavecapital, value in capitals.items():
        if val == value:
            return chavecapital
    
def chave_estado(val):
    statess = states()
    for chavestado, value in statess.items():
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
