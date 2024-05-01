import Network
import Search
import matplotlib.pyplot as plt

result = Search.products("Samsung A15")
shopp_res = result["shopping_results"]
sources, cnt = Search.uniq_sources(shopp_res)
nodes2edges, weights = Network.get_nodes_edges(shopp_res)   

for src_ct in range(len(nodes2edges)):
    mapp = nodes2edges[src_ct]
    Gi = Network.graph_obj(mapp, weights[src_ct])
    Network.draw_G(Gi, mapp[0], weights[src_ct])
