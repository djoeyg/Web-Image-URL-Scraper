import requests
import bs4
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
            res = requests.get(input_json['recipe']['recipe_url'])
            soup = bs4.BeautifulSoup(res.text, 'lxml')
            search = soup.find(attrs={"class": "icon-image-zoom"})
            if search is None:
                raise NotFoundError
            image_link = search.get('data-image')
            input_json['recipe']['image_url'] = image_link
            return jsonify(input_json)

        except NotFoundError:
            input_json = request.get_json()
            abort(404, description=f"Unable to retrieve image of recipe from {input_json['recipe']['recipe_url']}")


api.add_resource(RecipeImage, '/')
