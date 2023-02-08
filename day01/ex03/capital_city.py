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
        states_list = statess()
        result = capital_cities()
        final = result.get(states_list.get(input)) 
        if input in states_list.keys():
            print(final)
        else: sys.exit("Unknown state.")

if __name__ == '__main__':
    getstate()
