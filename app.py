#!bin/python
from flask import Flask, jsonify
from getrecipe import get_recipe

app = Flask(__name__)

l = [
    {'a': 1, 'b': 2},
    {'c': 3, 'd': 4}
]


@app.route('/api/recipe/tasks', methods=['GET'])
def getTasks():
    return jsonify({'tasks': l})


@app.route('/api/<string:ing>', methods=['GET'])
def get_task(ing):
    # task = [task for task in tasks if task['id'] == task_id]
    # if len(task) == 0:
    #     abort(404)
    # ing = 'shredded chicken,'
    # get_r =
    obj = get_recipe(ing, 1)
    return obj.return_recipe()
    # print get_r.return_recipe.content
    # return jsonify(l)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
