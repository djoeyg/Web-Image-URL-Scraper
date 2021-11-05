import requests
import bs4

from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class RecipeImage(Resource):
    #def get(self):
    #    return {'about': 'All-Recipes Images Downloader'}

    def post(self):
        some_json = request.get_json()

        res = requests.get(some_json['url'])
        soup = bs4.BeautifulSoup(res.text, 'lxml')

        search = soup.find(attrs={"class": "icon-image-zoom"})
        image_link = search.get('data-image')
        print(image_link)

        return {'img_url': image_link}, 201


api.add_resource(RecipeImage, '/')

if __name__ == '__main__':
    app.run(debug=True)
