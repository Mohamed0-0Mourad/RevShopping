import plotly.express as px 
import numpy as np
import pandas as pd 

def avg(prices:list)->float:
    return sum(prices)/len(prices)

def stats_dict(shopp_res: list[dict], weights: list ) -> dict:
    src_price = dict()
    src_discount= dict()
    for i, res in enumerate(shopp_res):
        try:
            price = res['extracted_price']
            old = res['extracted_old_prices']
            src = res['source']
        except KeyError:
            continue
        
        discount = old - price

        try:
            src_price[src].append(price)
            src_discount[src].append(discount)
        except KeyError:
            src_price[src] = [price]
            src_discount[src] = [discount]

    for key in src_price:
        src_price[key] = avg(src_price[key])
        src_discount[key] = avg(src_discount[key])
    df_dict = {"Sources": list(src_price.keys()), "Average Prices": list(src_price.values()), "Average Discounts": list(src_discount.values()), "Weight(rate*reviews)": weights}
    return df_dict

def dashboard(df_dict: dict):
    df = pd.DataFrame(df_dict)
    