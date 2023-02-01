import sys

states = {
"Oregon" : "OR",
"Alabama" : "AL",
"New Jersey": "NJ",
"Colorado" : "CO"
}
capital_cities = {
"OR": "Salem",
"AL": "Montgomery",
"NJ": "Trenton",
"CO": "Denver"
}

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

getstate()
