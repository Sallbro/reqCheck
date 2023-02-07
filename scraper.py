from bs4 import BeautifulSoup
import requests


def get_url(suggestion_url):
    # page = requests.get("https://store.steampowered.com/search/suggest?term=spo&f=games&cc=IN&realm=1&l=english&v=17639006&excluded_content_descriptors%5B%5D=3&excluded_content_descriptors%5B%5D=4&use_store_query=1&use_search_spellcheck=1");
    page = requests.get(suggestion_url)

    results = BeautifulSoup(page.content, "html.parser")
    # print("res: ",results);
    url_attribute = results.find("a")
    url = url_attribute.get("href")
    print("\n url: ", url)

    return url


def get_requirements(suggestion_url):
    minVal = {}
    recVal = {}
    print("LOLLLLLLLL:-----------------------------")
    page = requests.get(get_url(suggestion_url))
    results = BeautifulSoup(page.content, "html.parser")
    # print(results.prettify());

    print("\n minimum...")
    minimumReq = results.find_all(
        "div", {"class": "game_area_sys_req_leftCol"});
    if len(minimumReq) == 0:
        test = results.find("div", {"class": "sysreq_contents"})
        minimumReq = test.find_all(
            "div", {"data-os": "win"},
        )

    for thing in minimumReq:
        i = thing.find_all("li")
        for x in i:
            if(len(x.get_text().split(":")) > 1):
                key = x.get_text().split(":")[0]
                value = x.get_text().split(":")[1]
                minVal[key] = value
        print(minVal)

    print("\n recomdedReq...")
    recomdedReq = results.find_all(
        "div", {"class": "game_area_sys_req_rightCol"})
    for thing in recomdedReq:
        i = thing.find_all("li")
        for x in i:
            if(len(x.get_text().split(":")) > 1):
                key = x.get_text().split(":")[0]
                value = x.get_text().split(":")[1]
                recVal[key] = value
        print(recVal)

    return {"min": minVal, "recommended": recVal}
