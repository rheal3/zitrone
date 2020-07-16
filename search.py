import json

# Search Functions
def append_record(dictionary):
    with open('ingredient_search', 'a') as file:
        json.dump(dictionary, file)
        file.write(os.linesep)

def access_record():
    ingredients_dictionary = {}
    with open('ingredient_search') as file:
        record_list = [json.loads(line) for line in file]
        for line in record_list:
            for key, value in line.items():
                if key not in ingredients_dictionary:
                    ingredients_dictionary[key] = value
                else:
                    ingredients_dictionary[key] += value
    return ingredients_dictionary

def search_by_ingredient(ingredient_to_find, ingredient_search):
    recipes_with_ingredient = []
    for ingredient in ingredient_search:
        if ingredient == ingredient_to_find:
            recipes_with_ingredient += ingredient_search[ingredient]
    return recipes_with_ingredient

def sort_recipes_by_most_ingredients(recipes_mult_ingredients):
    highest_value_recipe = ""
    highest_value = 0
    for recipe, amount in recipes_mult_ingredients.items():
        if amount > highest_value:
            highest_value_recipe = recipe
    return highest_value_recipe
