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

# if input_tratado == capital:
#     print (x)
# else: print (y)                                                                                                                         

def chave_capital(val):
    for key, value in capital_cities.items():
        if val == value:
            return value #retorna a capital qndo ela for digitada

def chave_estado(val):
    for chavestado, value in states.items():
        if val == chavestado:
            return (chavestado)

def input():
    return input

def all_in():
    input = sys.argv[1] 
    input_tratado = input.split(",") #falta strip
    for i in input_tratado:
        capital = chave_capital(input_tratado)
        estado = chave_estado(input_tratado)  
        try:
            state, capital = find_state(arg)
        except:
            try:
                state, capital = find_capital(arg)
            except:
                pass
    if state != '':
        print(capital + " is the capital of " + state)
    elif arg != "":
        print( arg + " is neither a capital city nor a state")

    all_in()
  
# The program must take for argument a string containing as many expressions as
# we search for, separated by a coma.
# • For each expression in this string, the program must detect if it’s a capital, a state
# or none of them.
# • The program must not be case-sensitive. It must not take multiple spaces in consideration either.
# • If there is no parameter or too many parameters, the program doesn’t display
# anything.
# • When there are two successive comas in the string, the program doesn’t display
# anything.