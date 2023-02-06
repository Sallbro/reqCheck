from scraper import get_requirements
from flask import Flask
import requests

app = Flask(__name__)


@app.route("/")
def lol():
    return "lol"


@app.route("/get/")
def get():
    url = "https://store.steampowered.com/search/suggest?term=spo&f=games&cc=IN&realm=1&l=english&v=17639006&excluded_content_descriptors%5B%5D=3&excluded_content_descriptors%5B%5D=4&use_store_query=1&use_search_spellcheck=1"
    res = get_requirements(url)
    return res


if __name__ == '__main__':
    app.run()


# https://store.steampowered.com/search/suggest?term=str&f=games&cc=US&realm=1&l=english&v=17631244&excluded_content_descriptors[]=3&excluded_content_descriptors[]=4&use_store_query=1&use_search_spellcheck=1
