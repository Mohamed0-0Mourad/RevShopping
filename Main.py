import Network
import Search
import matplotlib.pyplot as plt
import math

result = Search.products("Macbook M3")
shopp_res = result["shopping_results"]
sources, cnt = Search.uniq_sources(shopp_res)
nodes2edges = Network.get_nodes_edges(shopp_res)   

for src_ct in range(len(nodes2edges)):
    mapp = nodes2edges[src_ct]
    Gi = Network.graph_obj(mapp)
    Network.draw_G(Gi, mapp[0])

