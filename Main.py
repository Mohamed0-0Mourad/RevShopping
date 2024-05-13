import Stats
import Search
import Network
import Map
import PySimpleGUI as sg
import Find 

q = ''
api_key = ''
layout = [  [sg.Text("Search a product: \nIt can be any shopping product. \t(for semantic heatmap it must be electronic)", background_color='#56BF81')],
            [sg.InputText(size = 70)],
            [sg.Text("Enter your SerpApi key\nIf you don't have a one head to (https://serpapi.com/users/sign_up) and sign up.", background_color='#56BF81')],
            [sg.InputText(size = 70)],
            [sg.Button('Search', button_color='#7E70AD'), sg.Button('Exit', button_color="red")] ]


window = sg.Window('RevShopping', layout, background_color='#56BF81')

event, values = window.read()

if event == 'Search':
    q = values[0]
    api_key = values[1]

if q != '' and api_key != '':
    sg.popup(f'Searching {values[0]}...', no_titlebar=True, auto_close=True, auto_close_duration=5, keep_on_top=True, modal=False, background_color="#56BF81", button_color="#7E70AD")
    result = Search.products(q, api_key)
    shopp_res = result["shopping_results"]
    cnt, sources = Search.uniq_sources(shopp_res)
    nodes2edges, weights, revURL = Network.get_nodes_edges(shopp_res)   
    layout = [[sg.Text("Product Analysis Done!\n\nChoose from the analysis options below:\n", background_color="#56BF81")],
            [sg.Button("Plots Dashboard")],
            [sg.Button('Shop-Product Network'), sg.Button('Reviews Sentemint Analysis')], 
            [sg.Button('Get product link(by source)')],
            [sg.Button("Exit", button_color="red")] 
            ]
    window = sg.Window('RevShopping', layout, background_color="#56BF81", button_color="#7E70AD")
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

        elif event == 'Get product link(by source)':
            find = sg.popup_get_text("Enter Source Name (case sensetive): ", background_color="#56BF81", button_color='#7E70AD')
            df_dict = Find.find_nodes(find, nodes2edges, weights, shopp_res)
            Find.dashboard(df_dict)
            out = "Links with respect to order of positions:\n"
            for i, l in enumerate(df_dict["Links"]):
                out+=f"{i+1}- {l}"
                out += '\n\n'
            sg.popup(out, title = "Links", background_color="#56BF81", button_color='#7E70AD')
        elif event == "Exit" or event == sg.WIN_CLOSED:
            break

    window.close()
else:
    sg.popup_error("Sorry, one of the feilds has not been filled", title = "Field Error!", background_color='#56BF81')