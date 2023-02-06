from scraper import get_requirements
from flask import Flask, render_template, request,redirect, url_for
import requests

app = Flask(__name__)


@app.route("/")
def lol():
    return render_template('search.html')


@app.route("/get", methods=['POST', 'GET'])
def get():
    if request.method == 'POST':
        print(request.form)
        search_val = request.form["search"]
        print("search_val:", search_val)
        # url_test = "https://store.steampowered.com/search/suggest?term=spo&f=games&cc=IN&realm=1&l=english&v=17639006&excluded_content_descriptors%5B%5D=3&excluded_content_descriptors%5B%5D=4&use_store_query=1&use_search_spellcheck=1"
        url = 'https://store.steampowered.com/search/suggest?term=%s' % search_val + \
            '&f=games&cc=IN&realm=1&l=english&v=17639006&excluded_content_descriptors%5B%5D=3&excluded_content_descriptors%5B%5D=4&use_store_query=1&use_search_spellcheck=1'
        res = get_requirements(url)
        return res
    else:
        return redirect(url_for('lol'))


if __name__ == '__main__':
    app.run()


# https://store.steampowered.com/search/suggest?term=str&f=games&cc=US&realm=1&l=english&v=17631244&excluded_content_descriptors[]=3&excluded_content_descriptors[]=4&use_store_query=1&use_search_spellcheck=1
