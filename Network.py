import networkx as nx 
import matplotlib.pyplot as plt
from Search import uniq_sources

def get_nodes_edges(shopping_r: dict)-> list:    
    relations = {}
    
    for result in shopping_r:
        node = result["source"]
        p = f"{result['position']}. " + "{:,}".format(result['extracted_price']) + " EGP"
        try:
            relations[node].append(p)
        except KeyError:
            relations[node] = []
    
    node2edges = list(relations.items())

    # edges = []
    # for node in relations:
    #     for edge in relations[node]:
    #         edges.append((node, edge))
    
    return node2edges#, edges#, sizes

def graph_obj(mapp: tuple)-> nx.graph: 
    node = mapp[0]
    prods = mapp[1]
    G = nx.Graph()
    G.add_node(node, size = 2400, color = '#7E70AD', community = "Sites")
    
    for edge in prods:
        G.add_node(edge, size = 3800, color = '#56BF81', community = "Prices", font_weight = "bold")
        G.add_edge(node, edge, width = 3000)
    return G

def draw_G(G: nx.graph, centeral_node: str):
    colors = [node_data["color"] for node, node_data in G.nodes(data=True)]
    sizes = [node_data["size"] for node, node_data in G.nodes(data=True)]

    plt.clf()
    plt.plot(color = "#56BF81")
    nx.draw(G, with_labels = True, node_color=colors, node_size = sizes)
    x = plt.gca()
    x.margins(0.20)
    plt.axis(False)
    plt.savefig(f"{centeral_node}.png")
    plt.show()