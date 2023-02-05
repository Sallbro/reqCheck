from bs4 import BeautifulSoup
import requests


def get_url()
    page = requests.get("https://store.steampowered.com/search/suggest?term=str&f=games&cc=US&realm=1&l=english&v=17631244&excluded_content_descriptors[]=3&excluded_content_descriptors[]=4&use_store_query=1&use_search_spellcheck=1")
    results = BeautifulSoup(page.content, "html.parser")
    url = results.find("a")
    return url


def get_requirements(args):
    minVal={};
    recVal={};
    print("LOLLLLLLLL:-----------------------------")
    page = requests.get(get_url(args));
    print(page.content)
    results = BeautifulSoup(page.content, "html.parser");
    print("min...");
    minimumReq = results.find_all("div",{"class":"game_area_sys_req_leftCol"});
    for thing in minimumReq:
        i = thing.find_all("li")
        # lol = [print(x.get_text()) for x in i]
        for x in i:
            if(len(x.get_text().split(":")) >1):
                key = x.get_text().split(":")[0]
                value = x.get_text().split(":")[1]
                minVal[key] = value
        print(minVal)


    # print(results.prettify());
    print("\nrecomdedReq...");
    recomdedReq = results.find_all("div",{"class":"game_area_sys_req_rightCol"});
    for thing in recomdedReq:
        i = thing.find_all("li")
        # lol = [print(x.get_text()) for x in i]
        for x in i:
            if(len(x.get_text().split(":")) >1):
                key = x.get_text().split(":")[0]
                value = x.get_text().split(":")[1]
                recVal[key] = value
        print(recVal)

    return {"min":minVal, "recommended": recVal};