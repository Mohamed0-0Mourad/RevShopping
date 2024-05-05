import requests
import plotly.graph_objects as go 
import plotly
from plotly.subplots import make_subplots
import numpy as np
import pandas as pd
import Network

def access_dict(analysis: dict, key: str, value: int):
    try:   
        analysis[key] += value
    except KeyError: 
        analysis[key] = value  

def assign_scr(score: int, negatives: set, sent:str, words:set, drop:set, analysis:dict):
    if score >= 7:
        for ne in negatives:
            if ne not in sent:
                for pos in words:
                    if pos in drop or pos.isnumeric() or not pos.isprintable():
                        continue
                    else:
                        access_dict(analysis, pos, 1)
            else:
                for neg in words:
                    if neg in drop or neg.isnumeric() or not neg.isprintable():
                        continue
                    else:
                        access_dict(analysis, neg, -1.5)

    elif score >= 4:
        for ne in negatives:
            if ne not in sent:
                for pos in words or pos.isnumeric() or not pos.isprintable():
                    if pos in drop:
                        continue
                    else:
                        access_dict(analysis, pos, 0.25)
            else:
                for neg in words:
                    if neg in drop or neg.isnumeric() or not neg.isprintable():
                        continue
                    else:
                        access_dict(analysis, neg, -0.25)
    elif score >= 0 :
        for ne in negatives:
            if 'but' in sent:
                for pos in words or pos.isnumeric():
                    if pos in drop:
                        continue
                    else:
                        access_dict(analysis, pos, 1.5)
            else:
                for neg in words:
                    if neg in drop or neg.isnumeric() or not neg.isprintable():
                        continue
                    else:
                        access_dict(analysis, neg, -1)


def analys(js2dict: dict, query:str) -> dict:           # -----------------------------------------> MAAAAAINNN
    analysis = dict()
    while True:
        reviews = js2dict['reviews']

        # scores = []
        drop = {query.lower().split()[0],'،','with', 'phone', 'mobile', "it's", "can't", 'he', 'had', 'not', 'and', 'a', 'the', 'you', 'have',"i'm", 'this', 'these', 'that', 'so', 'be', 'am', 'on', 'is', 'to', 'i', 'my', 'me', 'it', 'of', 'in', 'for', 'was', "hate", "dislike", 'but', 'do', 'not', "don't", 'like', 'love', 'greates', 'fan', 'myself', 'from', 'one', 'few', 'diffrent', 'thing', 'things', '', 'any', "can't", 'see', 'at', 'it'}
        negatives = {"hate", "dislike", 'but',"i don't like", "i do not like"}

        for rev in reviews:
            score = rev['score']
            # scores.append(score)
            txt = rev['extract'].lower().split('.')
            for sent in txt:
                words = sent.split(" ")
                assign_scr(score, negatives, sent, words, drop, analysis)
                                      
        try:
            link = js2dict['next-page-url']
            link = link.replace('ar', 'en')
            r2 = requests.get(link)
            js2dict = r2.json()
        except KeyError:
            break
    return analysis

def draw_heatmap(analysis:dict):
    y = pd.Series(analysis.keys())
    scores = np.array(list(analysis.values()))
    di = {"Score(ranging from bad - neutral - good)": scores, "Word": y.index}
# https://plotly.com/python/line-and-scatter/
# https://plotly.com/python/discrete-color/
#https://plotly.com/python/builtin-colorscales/

    df = pd.DataFrame(di)
    bar=dict(
    title="How much it appeared in reviews",
    thicknessmode="pixels", thickness=50,
    lenmode="pixels", len=400,
    yanchor="top", y=1,
    ticks="outside", ticksuffix= "Score(ranging from bad - neutral - good)",
    dtick=5
    )

    fig = make_subplots(1, 2, shared_yaxes=True, shared_xaxes=True, column_titles=("Product Review Specification (Using Word Score) from B.TECH", "Heatmap (Red: -, Yellow: neutral, Green: +)"))
    fig.add_trace(go.Scatter(y= y.values, x= scores),row=1, col = 1)
    fig.add_trace(go.Heatmap(x=scores, y=y.values, z=scores , colorbar=bar, colorscale=plotly.colors.diverging.RdYlGn), row = 1, col=2)
    fig.show()
