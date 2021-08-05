import pytest
import functions

recipes = [
    {'recipe name': 'Strong Cheese',
        'calories': 2201, 'meal_type': 'snack'},
    {'recipe name': 'Cheese Crackers Recipe',
        'calories': 1097, 'meal_type': 'snack'},
    {'recipe name': 'Pimento Cheese',
        'calories': 2726, 'meal_type': 'lunch/dinner'},
    {'recipe name': 'Goat Cheese Soufflé',
        'calories': 1000, 'meal_type': 'brunch'},
    {'recipe name': 'Goat Cheese Frosting',
        'calories': 2383, 'meal_type': 'teatime'}
]


def test_sort_recipes_by_calories():
    validator = functions.sort_recipes(recipes, 'calories')
    expected = [
        {'recipe name': 'Goat Cheese Soufflé',
            'calories': 1000, 'meal_type': 'brunch'},
        {'recipe name': 'Cheese Crackers Recipe',
            'calories': 1097, 'meal_type': 'snack'},
        {'recipe name': 'Strong Cheese',
            'calories': 2201, 'meal_type': 'snack'},
        {'recipe name': 'Goat Cheese Frosting',
            'calories': 2383, 'meal_type': 'teatime'},
        {'recipe name': 'Pimento Cheese',
         'calories': 2726, 'meal_type': 'lunch/dinner'},
    ]
    assert validator == expected


def test_sort_recipes_by_name():
    validator = functions.sort_recipes(recipes, 'recipe name')
    expected = [
        {'recipe name': 'Cheese Crackers Recipe',
         'calories': 1097, 'meal_type': 'snack'},
        {'recipe name': 'Goat Cheese Frosting',
         'calories': 2383, 'meal_type': 'teatime'},
        {'recipe name': 'Goat Cheese Soufflé',
         'calories': 1000, 'meal_type': 'brunch'},
        {'recipe name': 'Pimento Cheese',
         'calories': 2726, 'meal_type': 'lunch/dinner'},
        {'recipe name': 'Strong Cheese',
         'calories': 2201, 'meal_type': 'snack'},
    ]
    assert validator == expected


def test_add_key_meal_type_if_it_does_not_exist():
    recipes = [
        {'recipe':
         {'label': 'Pasta alla Gricia Recipe'}},
        {'recipe':
         {'label': 'Pasta Frittata Recipe'}}, ]
    validator = functions.add_key_meal_type_if_it_does_not_exist(recipes)
    print(functions.add_key_meal_type_if_it_does_not_exist(recipes))
    expected = [
        {'recipe':
         {'label': 'Pasta alla Gricia Recipe', 'mealType': 'lunch, dinner'}},
        {'recipe':
         {'label': 'Pasta Frittata Recipe', 'mealType': 'lunch, dinner'}}, ]

    assert validator == expected


def test_save_search():

    recipes = [{'recipe':
                {'label': 'Strong Cheese', 'url': 'http://notwithoutsalt.com/strong-cheese/',
                 'calories': 2201.3315221999997, 'mealType': 'snack'}},
               {'recipe':
                {'label': 'Pimento Cheese', 'url': 'http://www.lottieanddoof.com/2009/05/pimento-cheese/',
                 'calories': 2726.7639985500005, 'mealType': 'lunch/dinner'}}, ]
    validator = functions.save_search(recipes)
    expected = [
        {'recipe name': 'Strong Cheese', 'url': 'http://notwithoutsalt.com/strong-cheese/',
         'calories': 2201.3315221999997, 'meal type': 'snack'},
        {'recipe name': 'Pimento Cheese', 'url': 'http://www.lottieanddoof.com/2009/05/pimento-cheese/',
         'calories': 2726.7639985500005, 'meal type': 'lunch, dinner'}]
    assert validator == expected


def test_save_meal_type():
    meal_types = [
        {'meal type': 'breakfast'}, {'meal type': 'dinner'},
        {'meal type': 'dinner'}, {'meal type': 'snacks'},
        {'meal type': 'dinner'}, {'meal type': 'lunch'},
        {'meal type': 'snacks'}, {'meal type': 'lunch'}]
    validator = functions.save_meal_type(meal_types)
    expected = {'breakfast', 'lunch', 'snacks', 'dinner'}
    assert validator == expected
