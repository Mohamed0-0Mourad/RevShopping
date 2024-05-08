import requests 
from bs4 import BeautifulSoup
import json
import Map

# r = requests.get("https://btech.com/en/apple-iphone-13-128gb-4gb-blue-jap.html")

# content = BeautifulSoup(r.content, "html5lib")

# allRev = content.select("div.reviews-show-more-button.btn-outline.primary.medium")
# link = allRev[0]['data-review-next-page-url']
# r2 = requests.get(link)
# js2dict = r2.json()

# analysis = Map.analys(js2dict, 'iphone 13')
# print(analysis)
# while True:
#     reviews = js2dict['reviews']

#     # scores = []
#     drop = {'he', 'had', 'not', 'and', 'a', 'the', 'you', 'have',"i'm", 'this', 'these', 'that', 'so', 'be', 'am', 'on', 'is', 'to', 'i', 'my', 'me', 'it', 'of', 'in', 'for', 'was', "hate", "dislike", 'but', 'do', 'not', "don't", 'like', 'love', 'greates', 'fan', 'myself', 'from', 'one', 'few', 'diffrent', 'thing', 'things', '', 'any', "can't", 'see', 'at', 'it'}
#     negatives = {"hate", "dislike", 'but',"i don't like", "i do not like"}

#     for rev in reviews:
#         score = rev['score']
#         # scores.append(score)
#         txt = rev['extract'].lower().split('.')
#         for sent in txt:
#             words = sent.split(" ")
#             if score >= 7:
#                 for ne in negatives:
#                     if ne not in sent:
#                         for pos in words:
#                             if pos in drop:
#                                 continue
#                             else:
#                                 try:   
#                                     analysis[pos] += 1
#                                 except KeyError: 
#                                     analysis[pos] = 1
#                     else:
#                         for neg in words:
#                             if neg in drop:
#                                 continue
#                             else:
#                                 try:   
#                                     analysis[pos] -= 1
#                                 except KeyError: 
#                                     analysis[pos] = -1    
#             elif score >= 4:
#                 for ne in negatives:
#                     if ne not in sent:
#                         for pos in words:
#                             if pos in drop:
#                                 continue
#                             else:
#                                 try:   
#                                     analysis[pos] += 0.5
#                                 except KeyError: 
#                                     analysis[pos] = 0
#                     else:
#                         for neg in words:
#                             if neg in drop:
#                                 continue
#                             else:
#                                 try:   
#                                     analysis[pos] -= 0.5
#                                 except KeyError: 
#                                     analysis[pos] = 0
#             elif score >= 0 :
#                 for ne in negatives:
#                     if 'but' in sent:
#                         for pos in words:
#                             if pos in drop:
#                                 continue
#                             else:
#                                 try:   
#                                     analysis[pos] += 1.5
#                                 except KeyError: 
#                                     analysis[pos] = 1.5
#                     else:
#                         for neg in words:
#                             if neg in drop:
#                                 continue
#                             else:
#                                 try:   
#                                     analysis[pos] -= 1
#                                 except KeyError: 
#                                     analysis[pos] = -1                      
#     try:
#         link = js2dict['next-page-url']
#         r2 = requests.get(link)
#         js2dict = r2.json()
#     except KeyError:
#         break
# print(analysis)

# # fast: from high score, then it must be positive 
# import pandas as pd
# import numpy as np 
# import plotly.express as px

# y = pd.Series(analysis.keys())
# scores = np.array(list(analysis.values()))

# x_grid = np.arange(min(scores), max(scores), 0.25)
# y_grid = np.arange(min(y.index), max(y.index), 1)
# x_mesh, y_mesh = np.meshgrid(x_grid, y_grid)

# z= []
# for r in range(x_mesh.shape[0]):
#     z_r = []
#     for c in range(y_mesh.shape[1]):
#         for i in range(scores.shape[0]):
#             if x_mesh[r,c] == scores[i] and y_mesh[r,c] == i:
#                 z_r.append(scores[i])
#             else:
#                 z_r.append(0)
#     z.append(z_r)


# di = {"Score(ranging from bad - neutral - good)": scores, "Word": y.index}
# https://plotly.com/python/line-and-scatter/
# https://plotly.com/python/discrete-color/
#https://plotly.com/python/builtin-colorscales/

# df = pd.DataFrame(di)

# heat = px.density_heatmap(df, nbinsx=20, nbinsy=20,color_continuous_scale=px.colors.diverging.RdYlGn, x = "Score(ranging from bad - good)", y= "Word", title = "Product Review Specification (Using Word Score) from B.TECH")
# sct = px.scatter(df, x = "Score(ranging from bad - good)", y= "Word", title = "Product Review Specification (Using Word Score) from B.TECH")
# bar=dict(
#     title="How much it appeared in reviews",
#     thicknessmode="pixels", thickness=50,
#     lenmode="pixels", len=400,
#     yanchor="top", y=1,
#     ticks="outside", ticksuffix= "Score(ranging from bad - neutral - good)",
#     dtick=5
# )
# heat.show()
# x_mesh.reshape((x_mesh.shape[0]*x_mesh.shape[1]))
# y_mesh.reshape((y_mesh.shape[0]*y_mesh.shape[1]))

# import plotly.graph_objects as go 
# import plotly
# from plotly.subplots import make_subplots
# fig = make_subplots(1, 2, shared_yaxes=True, shared_xaxes=True, column_titles=("Product Review Specification (Using Word Score) from B.TECH", "Heatmap (Red: -, Yellow: neutral, Green: +)"))
# fig.add_trace(go.Scatter(y= y.values, x= scores),row=1, col = 1)
# fig.add_trace(go.Heatmap(x=scores, y=y.values, z=scores , colorbar=bar, colorscale=plotly.colors.diverging.RdYlGn), row = 1, col=2)
# fig.show()

# https://pysimplegui.com 
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

# import PySimpleGUI as sg

# # All the stuff inside your window.
# layout = [  [sg.Text("Search a product: \nIt can be any electronic device.")],
#             [sg.InputText()],
#             [sg.Button('Search'), sg.Button('Exit')] ]

# # Create the Window
# window = sg.Window('RevShopping', layout)

# event, values = window.read()

# if event == 'Search':
#     sg.popup(f'Searching {values[0]}...', no_titlebar=True, auto_close=True, auto_close_duration=20)
#     q = values[0]
# window.close()

