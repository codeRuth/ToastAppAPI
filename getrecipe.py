import requests
import json

API_KEY = 'a7117cb7dc7f8b768ec323b949e752dd'


class getRecipe(object):
    def __init__(self, ingredient, page):
        self.list = ingredient
        self.page = page

    def is_valid(inp):
        valid_publishers = ['All Recipes', 'Back to Her Roots', 'BBC Food', 'BBC Good Food', 'Bon Appetit',
                            'Bunky Cooks', 'Chow', 'Closet Cooking', 'Cookin Canuck', 'Epicurious', 'Food Republic',
                            'Framed Cooks', 'Healthy Delicious', 'Jamie Oliver', "Lisa's Kitchen"]
        for i in range(len(valid_publishers)):
            if inp == valid_publishers[i]:
                return True
        return False

    def return_recipe(self):
        response = []
        num = 0
        page = requests.get('http://food2fork.com/api/search?key=' + API_KEY +
                            '&q=' + self.list +
                            '&page=' + str(self.page))
        parsed = json.loads(page.text)
        count = parsed['count']

        for i in range(0, count):
            if is_valid(parsed['recipes'][i]['publisher']):
                temp = json.dumps({'title': parsed['recipes'][i]['title'],
                                   'id': parsed['recipes'][i]['recipe_id']},
                                  separators=(',', ':'))
                response.append(temp)
                num += 1
        return str(response).replace("'", '')


if __name__ == '__main__':
    obj = getRecipe("shredded chicken", 1)
    obj.return_recipe()
