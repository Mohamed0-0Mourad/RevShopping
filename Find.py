import pandas as pd 
import plotly.express as px
from Network import norm
def find_nodes(search: str, nodes2edges: list, weights, shopp_res):
    for i, n_map in enumerate(nodes2edges):
        if n_map[0] == search:
            scatters = n_map[1]
            x = []
            y = []
            z = []
            for j, node in enumerate(scatters):
                node = node.split('-')
                x.append(int(node[0]))
                p = node[1][:-4]
                p = p.replace(',', '')
                y.append(float(p))
                z.append(weights[i][j])
    if x == []:
        print("Error in search query. please make sure you enter a valid source name")
        return
    
    links = find_links(shopp_res, x)
    dict_df = {"Position": x, "Price": y, "Trust (rate*reviews)":z, "Links": links}
    return dict_df

def find_links(shopp_res, positions:list):
    links = []
    for i in positions:
        l= shopp_res[i-1]['link']
        links.append(l)
    return links

def dashboard(df_dict:dict):
    df = pd.DataFrame(df_dict)
    # normalized = norm(df["Trust (rate*reviews)"])
    fig = px.scatter_3d(df, x="Position", y= "Price", z = "Trust (rate*reviews)", text="Price", title=f"Relation between price and trust", hover_data="Links")
    fig.show()
    #[norm*1000 for norm in normalized]