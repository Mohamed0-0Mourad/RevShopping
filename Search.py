from serpapi import GoogleSearch
import requests 
from bs4 import BeautifulSoup
import json

def products(product: str, location: str = "eg"):
    if len(location) != 2:
      print("Sorry the location should be two characters according to Google countries abbreviation")
      return

    params = {
    "engine": "google_shopping",
    "q": product,
    "gl": location,
    "hl": "en",
    "api_key": "b571bb3042722702eb99ff8deeee9a929f0cf3d893ed9b204423ce72a42f06d6"
    }   
    results = GoogleSearch(params).get_dict()
    return results

def get_title_abbrv(title: str, query:str):
    title = set(title.split())
    query = set(query.split())  
    t = title.difference(query)
    ret = " ".join(list(t))
    # t = " ".join(title[0:len(query)])
    return ret

def uniq_sources(shopping_results: dict)-> list:
    sources = list()
   
    for i, result in enumerate(shopping_results):
        try:
            sources.append(result['source'])
        except KeyError:
            del shopping_results[i]
            continue
    sources = set(sources)
    return list(sources), len(sources)

def get_reviews(url:str)-> dict:
    if url == '':
        print("Sorry, We couldn't get reviews because the product you are searching is not on B.TECH.")
        return
    r = requests.get("https://btech.com/en/apple-iphone-13-128gb-4gb-blue-jap.html")

    content = BeautifulSoup(r.content, "html5lib")

    allRev = content.select("div.reviews-show-more-button.btn-outline.primary.medium")
    link = allRev[0]['data-review-next-page-url']

    r2 = requests.get(link)
    js2dict = r2.json()
    return js2dict