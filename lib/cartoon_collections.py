def roll_call_dwarves(list):
    for name in list:
        print(f"{list.index(name) + 1}. {name}")
    pass

def summon_captain_planet(list):
    new_list = []
    for item in list:
        new_list.append(f"{item.capitalize()}!")
    return new_list
    pass

def long_planeteer_calls(list):
    value = False
    for name in list:
        if len(name) > 4:
            value= True
    return value
    
    pass

def find_the_cheese(list):
    for item in list:
        if item == "cheddar" or item == "gouda" or item == "cheese" or item == "camembert":
            return item
    pass
