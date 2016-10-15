#!bin/python
from flask import Flask, jsonify
from get_recipe import getRecipe
from get_detail import getDetail

app = Flask(__name__)


@app.route('/recipe/<string:recipe_id>', methods=['GET'])
def get_recipe(recipe_id):
    obj = getDetail(recipe_id)
    return jsonify(obj.return_detail())


@app.route('/recipes/<string:ing>', methods=['GET'])
def get_recipes(ing):
    obj = getRecipe(ing, 1)
    return jsonify(obj.return_recipe())

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
