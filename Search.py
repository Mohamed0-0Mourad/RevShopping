from serpapi import GoogleSearch

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
