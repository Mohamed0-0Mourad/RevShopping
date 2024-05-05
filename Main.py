import Network
import Search
import matplotlib.pyplot as plt
import tkinter as tk
import Map

# root = tk.Tk()
# root.title("RevShopping")

# frm = tk.Frame(root, relief= "ridge", padx=10, pady=10)
# frm.grid()

# labl = tk.Label(frm, text= "Search a product: ")
# labl.grid(column=249, row = 149)

# # global q, entry
# q = tk.StringVar()

# def inp():
#     q = entry.get()
#     print(f"Searching {q}")

# entry = tk.Entry(frm, textvariable= q, width= 40)
# entry.grid(column=250, row=150)       #https://tkdocs.com/widgets/entry.html, https://tkdocs.com/tutorial/widgets.html#entry

# btn = tk.Button(frm, text="Search!", command= inp)
# btn.grid(column=499, row= 299)

# root.mainloop()           #https://docs.python.org/3/library/tkinter.html#entry
# print(f"Input {q}")

q ="Macbook M1"

result = Search.products(q)
shopp_res = result["shopping_results"]
sources, cnt = Search.uniq_sources(shopp_res)
nodes2edges, weights, revURL = Network.get_nodes_edges(shopp_res)   

for src_ct in range(len(nodes2edges)):
    mapp = nodes2edges[src_ct]
    Gi = Network.graph_obj(mapp, weights[src_ct])
    Network.draw_G(Gi, mapp[0], weights[src_ct])

# Mapping
reviews = Search.get_reviews(revURL)

analysis = Map.analys(reviews, q)

Map.draw_heatmap(analysis)
