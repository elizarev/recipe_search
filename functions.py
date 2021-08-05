from numpy import PINF
import pandas as pd
from tabulate import tabulate
import requests
import csv


def recipe_search(ingredient):
    result = requests.get(
        f'https://api.edamam.com/search?q={ingredient}&app_id=34e431dc&app_key=a9feb7ce55736d93127213120e7da496')
    data = result.json()
    return data['hits']


def add_key_meal_type_if_it_does_not_exist(recipes):
    for recipe in recipes:
        if 'mealType' not in recipe['recipe']:
            recipe['recipe'].update({'mealType': 'lunch, dinner'})
    return recipes


def table_format(recipes):
    pf = pd.DataFrame(recipes)
    return tabulate(pf, headers='keys', tablefmt='psql', floatfmt=".1f")


def save_search(recipe):
    recipes_saved = []
    for item in recipe:
        calories = item['recipe']['calories']
        meal_type = ''.join(item['recipe']['mealType'])
        if meal_type == 'lunch/dinner':
            meal_type = 'lunch, dinner'
        label = item['recipe']['label']
        url = item['recipe']['url']
        recipes_saved.append(
            {'recipe name': label, 'url': url, 'calories': calories, 'meal type': meal_type})
    print(table_format(recipes_saved))
    return recipes_saved


def save_meal_type(recipes_saved):
    return((set(map(lambda recipe: recipe['meal type'], recipes_saved))))


def filter_by_meal_type(mealtype_selected, recipes_saved):
    meal_type_in_recipes = save_meal_type(recipes_saved)
    if (mealtype_selected == 'lunch') or (mealtype_selected == 'dinner'):
        recipe_filtered = list(filter(
            lambda recipe: recipe['meal type'] == 'lunch, dinner', recipes_saved))
        print(table_format(recipe_filtered))
        return recipe_filtered
    if mealtype_selected in meal_type_in_recipes:
        recipe_filtered = list(filter(
            lambda recipe: recipe['meal type'] == mealtype_selected, recipes_saved))
        print(table_format(recipe_filtered))
        return recipe_filtered
    return recipes_saved


def sort_recipes(recipe, type_of_sort):
    sorted_items = sorted(
        recipe, key=lambda items: items[type_of_sort])
    print(table_format(sorted_items))
    return sorted_items


def save_results_in_csv_file(recipes_saved, ingredient):
    field_name = ['recipe name', 'url', 'calories', 'meal type']
    rows = []
    f = open(f'{ingredient}_recipes.csv', 'w')
    writer = csv.writer(f)
    writer.writerow(rows)
    f.close()
    with open(f'{ingredient}_recipes.csv', 'w+') as csv_file:
        spreadsheet = csv.DictWriter(csv_file, fieldnames=field_name)
        spreadsheet.writeheader()
        spreadsheet.writerows(recipes_saved)


def confirm(question):
    user_answer = input(f'{question} yes or no '.lower())
    if user_answer == 'yes':
        return True
    return False


def run_script(ingredient):
    recipes = save_search(add_key_meal_type_if_it_does_not_exist(
        (recipe_search(ingredient))))
    meal_type_in_recipes = save_meal_type(recipes)
    if len(meal_type_in_recipes) > 1:
        if confirm("Would you like to filter your results by the type of meal?"):
            meal_type_selected = input(
                f"Please write the type of meal that your prefer: {', '.join(save_meal_type(recipes)) } "
            ).lower()
            recipes = (filter_by_meal_type(meal_type_selected, recipes))
    if confirm("Would you like to sort your recipes by calories or name? "):
        type_of_sort = input(
            "Please type calories or name:  "
        ).lower()
        if type_of_sort == 'calories':
            recipes = sort_recipes(recipes, 'calories')
        if type_of_sort == 'name':
            recipes = sort_recipes(recipes, 'recipe name')
    if confirm("Would you like to save the results in a csv file?"):
        save_results_in_csv_file(recipes, ingredient)
    if confirm("Would you like to do another search?"):
        ingredient = input('Please type an ingredient: ')
        run_script(ingredient)
    return
