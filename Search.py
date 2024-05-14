from serpapi import GoogleSearch
import requests 
from bs4 import BeautifulSoup
import json

def products(product: str, api_key:str,location: str = "eg"):
    if len(location) != 2:
      print("Sorry the location should be two characters according to Google countries abbreviation")
      return

    params = {
    "engine": "google_shopping",
    "q": product,
    "gl": location,
    "hl": "en",
    "api_key": api_key
    }   
    results = GoogleSearch(params).get_dict()
    return results

# def get_title_abbrv(title: str, query:str):
#     title = set(title.split())
#     query = set(query.split())  
#     t = title.difference(query)
#     ret = " ".join(list(t))
#     # t = " ".join(title[0:len(query)])
#     return ret

def uniq_sources(shopping_results: dict)-> list:
    sources = []
   
    for i, result in enumerate(shopping_results):
        try:
            src = result['source']
        except KeyError:
            del shopping_results[i]
            continue
        if src not in sources:
            sources.append(src)
        
    
    sources = list(sources)
    num =len(sources)

    return num, sources

def get_reviews(url:str)-> dict:
    if url == '':
        print("Sorry, We couldn't get reviews because the product you are searching is not on B.TECH.")
        return
    url = url.replace('ar', 'en')
    r = requests.get(url)

    content = BeautifulSoup(r.content, "html5lib")

    allRev = content.select("div.reviews-show-more-button.btn-outline.primary.medium")
    try:
        link = allRev[0]['data-review-next-page-url']
    except IndexError: 
        print("Sorry! there's no reviews on this product on B.TECH")
        return
    r2 = requests.get(link)
    js2dict = r2.json()
    return js2dict