import requests
import bs4
import os
from flask import Flask, request, jsonify, abort
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

# Example POST requests in the terminal using curl:
# curl -H "Content-Type: Application/json" http://127.0.0.1:5000/ -X POST -d "{\"recipe\": {\"name\":\"Tango-Tofu-Tacos\",\"recipe_url\":\"https://www.allrecipes.com/recipe/228966/mango-tofu-tacos/\",\"image_url\":null}}"
# curl -H "Content-Type: Application/json" http://127.0.0.1:5000/ -X POST -d "{\"recipe\": {\"name\":\"Chicken-Marsala-With-Portobello-Mushrooms\",\"recipe_url\":\"https://www.allrecipes.com/recipe/72405/chicken-marsala-with-portobello-mushrooms/\",\"image_url\":null}}"
# curl -H "Content-Type: Application/json" http://127.0.0.1:5000/ -X POST -d "{\"recipe\": {\"name\":\"Juicy-Roasted-Chicken\",\"recipe_url\":\"https://www.allrecipes.com/recipe/83557/juicy-roasted-chicken/\",\"image_url\":null}}"


class NotFoundError(Exception):
    pass


class RecipeImage(Resource):

    def post(self):
        try:
            input_json = request.get_json()
            res = requests.get(input_json['recipe']['recipe_url'])
            soup = bs4.BeautifulSoup(res.text, 'lxml')
            search = soup.find(attrs={"class": "icon-image-zoom"})
            if search is None:
                raise NotFoundError
            image_link = search.get('data-image')
            input_json['recipe']['image_url'] = image_link
            return jsonify(input_json)
            # return jsonify({'image_url': image_link})

        except NotFoundError:
            input_json = request.get_json()
            abort(404, description=f"Unable to retrieve image of recipe from {input_json['recipe']['recipe_url']}")


api.add_resource(RecipeImage, '/')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5050))
    app.run(port=port, debug=True)
