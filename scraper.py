from bs4 import BeautifulSoup
import requests

def get_requirements(url):
    minVal={};
    recVal={};
    page = requests.get(url);
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

    return {"min":minVal, "max": recVal};