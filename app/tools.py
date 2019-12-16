import json


def count_recipe(ingredients):
    recipes = open('task.json', encoding='utf-8').read()
    recipes = json.loads(recipes)
    result = {}
    for recipe in recipes['recipes']:
        portion = {}
        i = 0
        for component in recipe['components']:
            if component['item'] not in ingredients:
                continue
            i += 1
            portion[component['item']] = ingredients[component['item']] // component['q']
            if i == len(recipe['components']):
                if min(portion.values()) == 0:
                    continue
                result[recipe['name']] = min(portion.values())
    return result
