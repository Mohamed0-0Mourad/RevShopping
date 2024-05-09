import plotly.express as px 
import numpy as np
import pandas as pd 
from Network import norm

def avg(prices:list)->float:
    return sum(prices)/len(prices)

def access_res(res:dict, sources, prices, discounts, delivery, condition):
    try:
        src = res['source']
    except KeyError:
        src = ""
    sources.append(src)
    try:
        price = res['extracted_price']
    except KeyError:
        price = 0
    prices.append(price)
    try:
        deliv = res['delivery']
        if deliv.isalnum():
            deliv = "Paid"
        else: 
            deliv = "Free"
    except KeyError:
        deliv = "Not Specified"
    delivery.append(deliv)
    try:
        old = res['extracted_old_prices']
    except KeyError:
        old= price
    discounts.append(old-price)
    try:
        cond = res["second_hand_condition"]
    except KeyError: cond = "New"
    condition.append(cond)

def stats_dict(shopp_res: list[dict], weights: list ) -> dict:
    sources  = list()
    prices = list()
    discounts= list()
    delivery = list()
    condition = list()
    for res in shopp_res:
        # try:
        #     src = res['source']
        #     price = res['extracted_price']
        #     old = res['extracted_old_prices']
        #     deliv= res['delivery']
        # except KeyError:
        #     continue
        access_res(res, sources, prices, discounts, delivery, condition)
        
        # discount = old - price
    ws = []
    for li in weights:
        li = norm(li)
        for w in li:
            ws.append(float(10+ w))
    df_dict = {"Position": range(1,len(shopp_res)+1),"Source": sources, "Price":prices, "Discount": discounts, "Trust(rate*reviews)": ws, "Delivery": delivery, "Condition": condition}
    return df_dict

def dashboard(df_dict: dict):
    df = pd.DataFrame(df_dict)
    fig = px.bar(df, x= "Position", y = "Price", color="Source", facet_col="Condition", hover_data=["Discount", "Delivery"])
    fig.show()
    #, width="Trust(rate*reviews)" ? ?? ? ?
