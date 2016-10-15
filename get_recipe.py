import requests
import json
import api_key


class getRecipe(object):
    def __init__(self, ingredient, page):
        self.list = ingredient
        self.page = page

    def return_recipe(self):
        response = []
        page = requests.get('http://food2fork.com/api/search?key=' + api_key.API_KEY +
                            '&q=' + self.list +
                            '&page=' + str(self.page))
        parsed = json.loads(page.text)
        count = parsed['count']

        for i in range(0, count):
            if is_valid(parsed['recipes'][i]['publisher']):
                temp = {
                    'title': parsed['recipes'][i]['title'],
                    'id': parsed['recipes'][i]['recipe_id']
                }
                response.append(temp)
        return response


def is_valid(inp):
    valid_publishers = ['All Recipes', 'Back to Her Roots', 'BBC Food', 'BBC Good Food', 'Bon Appetit',
                        'Bunky Cooks', 'Chow', 'Closet Cooking', 'Cookin Canuck', 'Epicurious', 'Food Republic',
                        'Framed Cooks', 'Healthy Delicious', 'Jamie Oliver', "Lisa's Kitchen"]
    for i in range(len(valid_publishers)):
        if inp == valid_publishers[i]:
            return True
    return False
