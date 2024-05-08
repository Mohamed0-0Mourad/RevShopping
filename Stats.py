import plotly.express as px 
import numpy as np
import pandas as pd 

def avg(prices:list)->float:
    return sum(prices)/len(prices)

def stats_dict(shopp_res: list[dict], weights: list ) -> dict:
    sources  = list()
    prices = list()
    discounts= list()
    delivery = list()
    for i, res in enumerate(shopp_res):
        try:
            src = res['source']
            price = res['extracted_price']
            old = res['extracted_old_prices']
            deliv= res['delivery']
        except KeyError:
            continue
        
        discount = old - price

        sources.append(src)
        prices.append(price)
        discounts.append(discount)
        delivery.append(deliv)
    # for key in src_price:
    #     src_price[key] = avg(src_price[key])
    #     src_discount[key] = avg(src_discount[key])
    df_dict = {"Position": range(1,len(shopp_res)),"Source": sources, "Price":prices, "Discount": discounts, "Trust(rate*reviews)": weights, "Delivery": delivery}
    return df_dict

def dashboard(df_dict: dict):
    df = pd.DataFrame(df_dict)
    fig = px.bar(df, x= "Discount", y = "Price", width="Trust(rate*reviews)", color="Sources", facet_col="Delivery")
    fig.show()