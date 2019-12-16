from app import app
from app.tools import count_recipe
from flask import request, jsonify


@app.route('/recipes', methods=['POST'])
def get_recipes():
    try:
        json = request.get_json()
        result = count_recipe(json)
        response = jsonify({'response': result})
        response.status_code = 200
        return response
    except Exception as err:
        app.logger.error("An error occurred {}".format(err))
        return jsonify({'error': err}), 400
