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
        if index in d_state:
            print(f'{d_state.get(index)} is the capital of {index}')
        elif index in d_capital:
            print(f'{index} is the capital of {d_capital.get(index)}')
        else: 
            print(f'{index} is neither a capital city nor a state')

if __name__ == '__main__':
	if (len(sys.argv) != 2):
		quit
	else:	
		all_in(sys.argv[1])
  