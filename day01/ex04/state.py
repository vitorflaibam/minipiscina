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

def capital_key(val):
    capitals = capital_cities()
    for capitalkey, value in capitals.items():
        if val == value:
            return capitalkey
    
def state_keys(val):
    statess = states()
    for statekey, value in statess.items():
        if val == value:
            return statekey
    return None

def run():
    if len(sys.argv) != 2:
        sys.exit(0)
    else:
        input = sys.argv[1]
        key_capitaltest = capital_key(input)
        statekey = state_keys(key_capitaltest)
        if statekey != None: 
            print(statekey)
        else:
            print("Unknown state.")

if __name__ == '__main__':
    run()
