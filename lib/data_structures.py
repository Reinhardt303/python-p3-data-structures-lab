spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    spicy_list =[]
    for food in spicy_foods:
        spicy_list.append(food["name"])
    return spicy_list
    # return [food["name"] for food in spicy_foods]    comprehension

def get_spiciest_foods(spicy_foods):
    spiciest_list = []
    for food in spicy_foods:
        if food["heat_level"] > 5:
            spiciest_list.append(food)
    return spiciest_list
#return [food for food in spicy_foods if food["heat_level"] > 5]

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶'*food['heat_level']}")
#print([f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶'*food['heat_level']}" for food in spicy_foods])

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food
# return [food for food in spicy_foods if food["cuisine"] == cuisine]

def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        if food["heat_level"] > 5:
            print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶'*food['heat_level']}")
            #print([f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶'*food['heat_level']}" for doos in spicy_foods if food["heat_level"] > 5])

def get_average_heat_level(spicy_foods):
    spice_level_list = []
    for food in spicy_foods:
        spice_level_list.append(food["heat_level"])
    average_heat_level = sum(spice_level_list) / len(spice_level_list)
    return average_heat_level


def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods

