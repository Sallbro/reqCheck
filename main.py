from scraper import get_requirements;
from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def lol():
    return "lol"


@app.route("/get/<>")
def get():
    res = get_requirements("stardew");
    return res

if __name__ == '__main__':
   app.run()


# https://store.steampowered.com/search/suggest?term=str&f=games&cc=US&realm=1&l=english&v=17631244&excluded_content_descriptors[]=3&excluded_content_descriptors[]=4&use_store_query=1&use_search_spellcheck=1