import Network
import Search
import matplotlib.pyplot as plt
import networkx as nx

result = Search.products("Macbook M3")

nodes, edges= Network.get_nodes_edges(result)
G = Network.graph_gen(nodes, edges)

plt.clf()
nx.draw_networkx(G, with_labels = True)
ax = plt.gca()
ax.margins(0.20)
plt.axis(False)
plt.show()
