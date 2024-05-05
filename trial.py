import requests 
from bs4 import BeautifulSoup
import json
import Map

r = requests.get("https://btech.com/en/apple-iphone-13-128gb-4gb-blue-jap.html")

content = BeautifulSoup(r.content, "html5lib")

allRev = content.select("div.reviews-show-more-button.btn-outline.primary.medium")
link = allRev[0]['data-review-next-page-url']
r2 = requests.get(link)
js2dict = r2.json()

analysis = Map.analys(js2dict, 'iphone 13')
# print(analysis)
# while True:
#     reviews = js2dict['reviews']

#     # scores = []
#     drop = {'he', 'had', 'not', 'and', 'a', 'the', 'you', 'have',"i'm", 'this', 'these', 'that', 'so', 'be', 'am', 'on', 'is', 'to', 'i', 'my', 'me', 'it', 'of', 'in', 'for', 'was', "hate", "dislike", 'but', 'do', 'not', "don't", 'like', 'love', 'greates', 'fan', 'myself', 'from', 'one', 'few', 'diffrent', 'thing', 'things', '', 'any', "can't", 'see', 'at', 'it'}
#     negatives = {"hate", "dislike", 'but',"i don't like", "i do not like"}

#     for rev in reviews:
#         score = rev['score']
#         # scores.append(score)
#         txt = rev['extract'].lower().split('.')
#         for sent in txt:
#             words = sent.split(" ")
#             if score >= 7:
#                 for ne in negatives:
#                     if ne not in sent:
#                         for pos in words:
#                             if pos in drop:
#                                 continue
#                             else:
#                                 try:   
#                                     analysis[pos] += 1
#                                 except KeyError: 
#                                     analysis[pos] = 1
#                     else:
#                         for neg in words:
#                             if neg in drop:
#                                 continue
#                             else:
#                                 try:   
#                                     analysis[pos] -= 1
#                                 except KeyError: 
#                                     analysis[pos] = -1    
#             elif score >= 4:
#                 for ne in negatives:
#                     if ne not in sent:
#                         for pos in words:
#                             if pos in drop:
#                                 continue
#                             else:
#                                 try:   
#                                     analysis[pos] += 0.5
#                                 except KeyError: 
#                                     analysis[pos] = 0
#                     else:
#                         for neg in words:
#                             if neg in drop:
#                                 continue
#                             else:
#                                 try:   
#                                     analysis[pos] -= 0.5
#                                 except KeyError: 
#                                     analysis[pos] = 0
#             elif score >= 0 :
#                 for ne in negatives:
#                     if 'but' in sent:
#                         for pos in words:
#                             if pos in drop:
#                                 continue
#                             else:
#                                 try:   
#                                     analysis[pos] += 1.5
#                                 except KeyError: 
#                                     analysis[pos] = 1.5
#                     else:
#                         for neg in words:
#                             if neg in drop:
#                                 continue
#                             else:
#                                 try:   
#                                     analysis[pos] -= 1
#                                 except KeyError: 
#                                     analysis[pos] = -1                      
#     try:
#         link = js2dict['next-page-url']
#         r2 = requests.get(link)
#         js2dict = r2.json()
#     except KeyError:
#         break
# print(analysis)

# # fast: from high score, then it must be positive 
import pandas as pd
import numpy as np 
import plotly.express as px

axis = pd.Series(analysis.keys())
scores = np.array(list(analysis.values()))
di = {"Score(ranging from bad - good)": scores, "Word": axis.values}
df = pd.DataFrame(di)
fig = px.scatter(df,x = "Score(ranging from negative - positive)", y= "Word", title = "Product Review Specification (Using Word Score) from B.TECH")
fig.show()

