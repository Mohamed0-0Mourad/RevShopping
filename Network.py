import networkx as nx 
import matplotlib.pyplot as plt

def get_nodes_edges(shopping_r: dict)-> list:    
    relations = {}
    all_weights = []
    
    BtechURL = []
    i= -1
    revs = 0
    for result in shopping_r:
        node = result["source"]
        if node == "B.TECH":
            try:
                curr_revs = result['reviews']
            except KeyError: curr_revs = 0

            if len(BtechURL) >= 1 and  curr_revs> revs:
                BtechURL = result['link']
            elif len(BtechURL)==0: 
                BtechURL.append(result['link'])
                revs = curr_revs
        
        p = f"{result['position']}. " + "{:,}".format(result['extracted_price']) + " EGP"
        
        try:
            rate = result["rating"]
            num_reviews = result['reviews']
        except KeyError:
            rate = 0.1
            num_reviews = 1

        try:
            relations[node].append(p)
            i = list(relations.keys()).index(node)
            all_weights[i].append(rate*num_reviews)
        except KeyError:
            relations[node] = []
            relations[node].append(p)
            all_weights.append(list())
            i= len(relations) -1
            all_weights[i].append(rate/num_reviews)
    
    node2edges = list(relations.items())
    if len(BtechURL) == 0:
        BtechURL ==""
    elif len(BtechURL) == 1: 
        return node2edges, all_weights, BtechURL[0]

    return node2edges, all_weights, BtechURL

def graph_obj(mapp: tuple, weights:list)-> nx.graph: 
    node = mapp[0]
    prods = mapp[1]
    G = nx.Graph()   
    G.add_node(node, size = 2400, color = '#7E70AD', font_weight = "bold")
    
    for i, edge in enumerate(prods):
        G.add_node(edge, size = 3800, color = '#56BF81', edge_weight = weights[i])
        G.add_edge(node, edge, width = 3000)
    return G

def norm(weights: list)->list:
    normalized = []
    mini = min(weights)
    maxi = max(weights)
    deno = maxi-mini
    if deno == 0: return weights

    for weight in weights:
        normalized.append((weight - mini)/deno)
    return normalized

def draw_G(G: nx.graph, centeral_node: str, weights: list):
    colors = [node_data["color"] for node, node_data in G.nodes(data=True)]
    sizes = [node_data["size"] for node, node_data in G.nodes(data=True)]
    # weights = [G.get_edge_data(edge[0], edge[1], default={"weight": None})["weight"] for edge in G.edges]
    # fonts = [node_data["font_weight"] for node, node_data in G.nodes(data=True)]

    pos = nx.spring_layout(G, seed= 300)   #https://networkx.org/documentation/stable/auto_examples/drawing/plot_edge_colormap.html#sphx-glr-auto-examples-drawing-plot-edge-colormap-py
    cmap = plt.cm.RdYlGn
    normalized = norm(weights)

    plt.clf()
    plt.plot(color = "#56BF81")
    nx.draw_networkx(G, node_color=colors, pos = pos, node_size = sizes, font_weight = "bold", font_size = 10, edge_color = cmap(normalized), width = [(5+norm) for norm in normalized])
    x = plt.gca()
    x.margins(0.20)
    plt.axis(False)
    try:
        plt.savefig(f"{centeral_node}.png")
    except OSError:
        return
    # plt.show()