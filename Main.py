import Stats
import Network
import Search
import matplotlib.pyplot as plt
import Map
import PySimpleGUI as sg

q = ''
layout = [  [sg.Text("Search a product: \nIt can be any electronic device.")],
            [sg.InputText()],
            [sg.Button('Search'), sg.Button('Exit')] ]


window = sg.Window('RevShopping', layout)

event, values = window.read()

if event == 'Search':
    q = values[0]
    sg.popup(f'Searching {values[0]}...', no_titlebar=True, auto_close=True, auto_close_duration=5, keep_on_top=True, modal=False)

if q != '':
    result = Search.products(q)
    shopp_res = result["shopping_results"]
    cnt, sources = Search.uniq_sources(shopp_res)
    nodes2edges, weights, revURL = Network.get_nodes_edges(shopp_res)   
    layout = [[sg.Text("Product Analysis Done!\n\nChoose from the analysis options below:\n")],
            [sg.Button("Plots Dashboard")],
            [sg.Button('Shop-Product Network'), sg.Button('Reviews Sentemint Analysis')], 
            [sg.Button('3D Graph')],
            [sg.Button("Exit")] 
            ]
    window = sg.Window('RevShopping', layout)
    while True:
        event, values = window.read()
        if event == "Plots Dashboard":
            df_dict = Stats.stats_dict(shopp_res, weights)
            Stats.dashboard(df_dict)

        elif event == "Shop-Product Network":
            for src_ct in range(len(nodes2edges)):
                mapp = nodes2edges[src_ct]
                Gi = Network.graph_obj(mapp, weights[src_ct])
                Network.draw_G(Gi, mapp[0], weights[src_ct])
            
            Network.plot_networks(sources, cnt)
        elif event == "Reviews Sentemint Analysis":
            reviews = Search.get_reviews(revURL)
            analysis = Map.analys(reviews, q)
            Map.draw_heatmap(analysis)
        # elif event == "3D Graph":

        elif event == "Exit" or event == sg.WIN_CLOSED:
            break

    window.close()