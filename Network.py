import networkx as nx 

def get_nodes_edges(results: dict)-> list:
    shopping_r = results["shopping_results"] 
    relations = {}
    nodes = list()
    # sizes = list()
    for result in shopping_r:
        node = result["source"]
        p = f"{result['position']}. {result['price']}"

        nodes.append(node)#; sizes.append(5) 
        nodes.append(p)#; sizes.append(8)
        try:
          relations[node].append(p)
        except KeyError:
          relations[node] = []
    
    edges = []
    for node in relations:
        for edge in relations[node]:
            edges.append((node, edge))
    
    return nodes, edges, #sizes

def graph_gen(nodes: list, edges:list)-> nx.graph:
  G = nx.Graph()
  
  for node in nodes:
    if node.isalpha():
      G.add_node(node, size = 50, color = 'red', community = "Sites")
    else: 
      G.add_node(node, size = 70, color = 'blue', community = "Prices")
  
  G.add_edges_from(edges)
  return G
