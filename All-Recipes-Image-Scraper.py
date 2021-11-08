import requests
import bs4
import os
from flask import Flask, request, jsonify, abort
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class NotFoundError(Exception):
    pass


class RecipeImage(Resource):

    def post(self):
        try:
            input_json = request.get_json()

            res = requests.get(input_json['url'])
            soup = bs4.BeautifulSoup(res.text, 'lxml')

            search = soup.find(attrs={"class": "icon-image-zoom"})
            if search is None:
                raise NotFoundError

            image_link = search.get('data-image')
            # print(image_link)
            return jsonify({'img_url': image_link})

        except NotFoundError:
            input_json = request.get_json()
            abort(404, description=f"Unable to retrieve image of recipe from {input_json['url']}")


api.add_resource(RecipeImage, '/')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5050))
    app.run(port=port, debug=True)

    # Example POST request using curl:
    # curl -H "Content-Type: Application/json" http://127.0.0.1:5000/ -X POST -d "{\"url\":\"https://www.allrecipes.com/recipe/228966/mango-tofu-tacos/\"}"
    # curl -H "Content-Type: Application/json" http://127.0.0.1:5000/ -X POST -d "{\"url\":\"https://www.allrecipes.com/recipe/72405/chicken-marsala-with-portobello-mushrooms/\"}"
    # curl -H "Content-Type: Application/json" http://127.0.0.1:5000/ -X POST -d "{\"url\":\"https://www.allrecipes.com/recipe/83557/juicy-roasted-chicken/\"}"
