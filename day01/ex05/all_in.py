import sys

def states():
    state = {
    "Oregon" : "OR",
    "Alabama" : "AL",
    "New Jersey": "NJ",
    "Colorado" : "CO"
    }
    return state

def capital_cities():
    capital_cities = {
    "OR": "Salem",
    "AL": "Montgomery",
    "NJ": "Trenton",
    "CO": "Denver"
    }
    return capital_cities                                                                                                                    

def all_in(str):
    stat = states()
    capital = capital_cities()

    d_state = {state: capital[UF] for state, UF in stat.items()}
    d_capital = {capital[UF]: state for state, UF in stat.items()}


    first_input = str.split(",")
    second_input = []
 
    for index in range(len(first_input)):
        if first_input[index].isspace() or first_input[index] == '':
            continue
        second_input.append(first_input[index].strip().title())

    for index in second_input:
        if second_input[index] in d_state:
            print(f'{d_state.get(second_input[index])} is the capital of {second_input[index]}')
        elif second_input[index] in d_capital:
            print(f'{second_input[index]} is the capital of {d_capital.get(second_input[index])}')
        else: 
            print(f'{second_input[index]} is neither a capital city nor a state')

if __name__ == '__main__':
	if (len(sys.argv) != 2):
		quit
	else:	
		all_in(sys.argv[1])
  
# The program must take for argument a string containing as many expressions as
# we search for, separated by a coma.
# • For each expression in this string, the program must detect if it’s a capital, a state
# or none of them.
# • The program must not be case-sensitive. It must not take multiple spaces in consideration either.
# • If there is no parameter or too many parameters, the program doesn’t display
# anything.
# • When there are two successive comas in the string, the program doesn’t display
# anything.