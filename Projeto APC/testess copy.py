from decimal import Overflow
from faulthandler import disable
from html.entities import html5
from tkinter import Button, font
from turtle import color
from click import style
import dash 
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from dash.exceptions import PreventUpdate
from dash import callback_context, no_update

import plotly.express as px
import plotly.graph_objects as go

import numpy as np
import pandas as pd
import json

####### 

#Array e dicicionários vazios para usar depois

anos = {}
ns = []
opcoes = {}

#Dicionários para usar no dropdown (selecionar)
#Estrutura dicionário -> dict = {"chave":"valor"}

geral1 = {"Desmatamento no Mundo":"Desmatamento no Mundo"}
america1 = {"Queimadas na América do Norte":"Queimadas na América do Norte"}
brasil1 = {'Desmatamento na Amazônia':"Desmatamento na Amazônia", 'Desmatamento no Cerrado':"Desmatamento no Cerrado"}
euro1 = {'Desmatamento na Europa':"Desmatamento na Europa"}
brasil_ce = {2019:"2019", 2020:"2020", 2021:"2021", "todos os anos":"todos os anos"}
brasil_am ={1998:"1998", 1999:"1999", 2000: "2000", 2001:"2001", 2002:"2002", 2003:"2003", 2004:"2004", 2005:"2005", 2006:"2006", 2007:"2007", 2008:"2008", 2009:"2009", 2010:"2010", 2011:"2011", 2012:"2012", 2013:"2013", 2014:"2014", "todos os anos":"todos os anos"}

###################### gráficos

maps = json.load(open("continente.json", "r")) #arquivo .json do mapa (gráfico 2)



### Dataframes para o mapa
dt = pd.read_csv("https://raw.githubusercontent.com/Arthrok/cerrado/main/cerrado%20(2).csv") #Cerrado
dk = pd.read_csv("https://raw.githubusercontent.com/Arthrok/cerrado/main/amazoniaestados.csv") #Amazonia
df = pd.read_csv('https://raw.githubusercontent.com/Dtcbsb/projeto/main/forestAreaChange.csv') #Europa
dn = pd.read_csv('https://raw.githubusercontent.com/LORliveira/desmatamento/main/Desmatamento%20dos%20continentes') #Continente




#cods do cerrado

tt1 = dt.values
ns = []
c3 = []
v1 = []
v2 = []
v3 = []
v4 = []

for i in range (len(tt1)): #33 linhas de dados
    v1.append(tt1[i][0]) #armazena os estados em v1
    if tt1[i][2] == 2021: #checa o ano
        v2.append(tt1[i][1]) #adiciona os valores do desmatamento em v2
    if tt1[i][2] == 2020:
        v3.append(tt1[i][1])
    if tt1[i][2] == 2019:
        v4.append(tt1[i][1])

#cods da amazônia
dk['qnt'] = dk['qnt'].astype(float)

#cods europa
df_array = df.values
vetor1 = [] 
for linha in df_array:
    vetor1.append(linha)

#cods continente
tabela_array = dn.values

Ano1 = []
Ano2 = []
Ano3 = [] 
Ano4 = []
for i in tabela_array:
    if i[1] == '1990':
        Ano1.append(i)
        if i[1] == '2000':
          Ano2.append(i)
        if i[1] == '2010':
          Ano3.append(i)
        if i[1] == '2015':
          Ano4.append(i)  



#==================================================
#Instanciação do dash

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])

#Dash Bootstrap
#Row cria esaços horizontais, o dbc container começa com uma ROW
#Col cria colunas
#Estrutura:
    #ROW (
    #   ROW(
    #       Col (
    # )
    #       Col(
    # )
    # )
    #   ROW(
    #       Col (
    # )
    #       Col (
    # )
    # ))



app.layout = dbc.Container(
    dbc.Row([
            dbc.Row([
                html.Div([
                    html.H1('teste')
                ], id="header")
            ]),
            dbc.Row([   ## Coluna dos integrantes do grupo e texto
                dbc.Col([ 
                    dbc.Row ([
                        dbc.Col ([
                            dbc.Card([
                                dbc.CardBody([
                                    html.Img(src=("https://cdn-icons-png.flaticon.com/512/711/711769.png"), height=51),
                                    html.H6( 'Arthur Alves Melo', style={"color": "#389fd6"}),
                                    html.H6( '211007856', style={"color": "#389fd6"}),               
                                ]),
                            ]),
                        ]),    
                        dbc.Col([
                            dbc.Card([
                                dbc.CardBody([
                                    html.Img(src=("https://cdn-icons-png.flaticon.com/512/711/711769.png"), height=51),
                                    html.H6( 'Arthur L. Mercadante', style={"color": "#389fd6"}),
                                    html.H6( '202028730', style={"color": "#389fd6"}),   
                                ])
                            ])
                        ]),
                        dbc.Col([
                            dbc.Card([
                                dbc.CardBody([
                                    html.Img(src=("https://cdn-icons-png.flaticon.com/512/711/711769.png"), height=51),
                                    html.H6( 'Davi Toledo da Costa', style={"color": "#389fd6"}),
                                    html.H6( '180118838 ', style={"color": "#389fd6"}),   
                                ])
                            ])
                        ]),                                                                                                                                         
                    ], id="n1"),
                    dbc.Row ([
                        dbc.Col ([
                            dbc.Card([
                                dbc.CardBody([
                                    html.Img(src=("https://cdn-icons-png.flaticon.com/512/711/711769.png"), height=51),
                                    html.H6( 'Filipe Ferreira Pereira', style={"color": "#389fd6"}),
                                    html.H6( '211061734', style={"color": "#389fd6"}),   
                                ]),
                            ]),
                        ]),    
                        dbc.Col([
                            dbc.Card([
                                dbc.CardBody([
                                    html.Img(src=("https://cdn-icons-png.flaticon.com/512/711/711769.png"), height=51),
                                    html.H6( 'Henrique M. Alencar', style={"color": "#389fd6"}),
                                    html.H6( '211061860', style={"color": "#389fd6"}),   
                                ])
                            ])
                        ]),
                        dbc.Col([
                            dbc.Card([
                                dbc.CardBody([
                                    html.Img(src=("https://cdn-icons-png.flaticon.com/512/711/711769.png"), height=51),
                                    html.H6( 'Henrique M. Fortes', style={"color": "#389fd6"}),
                                    html.H6( '211061879', style={"color": "#389fd6"}),   
                                ])
                            ])
                        ]),                                                                                                                                         
                    ], id="n2"),
                    dbc.Row ([
                        dbc.Col ([
                            dbc.Card([
                                dbc.CardBody([
                                    html.Img(src=("https://cdn-icons-png.flaticon.com/512/711/711769.png"), height=51),
                                    html.H6( 'Lucas O. Rodrigues', style={"color": "#389fd6"}),
                                    html.H6( '202017684', style={"color": "#389fd6"}),   
                                    
                                ]),
                            ]),
                        ]),    
                        dbc.Col([
                            dbc.Card([
                                dbc.CardBody([
                                    html.Img(src=("https://cdn-icons-png.flaticon.com/512/711/711769.png"), height=51),
                                    html.H6( 'Pedro Pinheiro Saad ', style={"color": "#389fd6"}),
                                    html.H6( '211062393', style={"color": "#389fd6"}),   
                                ])
                            ])
                        ]),
                        dbc.Col([
                            dbc.Card([
                                dbc.CardBody([
                                    html.Img(src=("https://cdn-icons-png.flaticon.com/512/711/711769.png"), height=51),
                                    html.H6( 'Walker D. A. Andrade', style={"color": "#389fd6"}),
                                    html.H6( '190096748', style={"color": "#389fd6"}),   
                                ])
                            ])
                        ]),                                                                                                                                         
                    ], id="n3"),                                                                                                                         
                ], md=5),
                dbc.Col([
                    dbc.Card ([
                        dbc.CardBody([
                            html.Span(
                                'Em prol do desenvolvimento tecnológico, a humanidade vem utilizando recursos naturais, tanto como matéria-prima, quanto como fonte energética. Como por exemplo, carvão, que é utilizado como combustível para diversas indústrias, e como matriz energética. Outro exemplo é a madeira, que tem diversos usos, em sua forma bruta, como matéria-prima para construções e artesanatos, em uma forma processada, pode se tornar papel, carvão vegetal, entre outras coisas.'
                                'No entanto, nos últimos 50 anos, surgiu uma discussão sobre a extração desmedida e desenfreada dos recursos naturais. Isso é decorrente de diversos estudos científicos relacionados ao aquecimento global. Um estudo que nos diz que as mudanças de temperatura no nosso planeta estão aumentando de frequência e intensidade, e que a tendência é que isso continue a aumentar se não nos dispusermos a controlar a extração e consumo de recursos naturais.'
                                'Dentre todos os problemas que ocorrem para a progressão do aquecimento global, um dos que nos chamam mais atenção é o desmatamento e as queimadas ilegais. '
                                'A gravidade do desmatamento se torna mais evidente quando pensamos que as árvores, colocadas como o pulmão do mundo, filtradoras de ar, grandes responsáveis pela manutenção de gases na atmosfera, como o oxigênio e gás carbônico, esse último sendo um dos responsáveis pela deterioração da camada de ozônio.'
                                'A UN FAO (Organização das Nações Unidas para Alimentação e Agricultura), estima que, desde 2010, 10 milhões de hectares de floresta foram derrubadas por ano, o pior é que, graças a essa mesma instituição, podemos afirmar que aproximadamente 50%, do número de arvores cortadas, foram plantadas para reflorestamento.'
                                'É importante dizer que apesar de termos trazido atenção para esse problema apenas no último século, o desflorestamento é algo que sempre esteve presente na história da humanidade, de toda a área terrestre do planeta apenas 71% é habitável, os outros 29% são inviáveis para vida humana de maneira sustentável, devido a gelo, desertos, entre outros problemas.'
                                'Pesquisas indicam que a 10.000 anos atrás, aproximadamente 57% dessa área era coberta em florestas, o equivalente a 6 Bilhões de Hectares, hoje em dia, no entanto, temos somente 4 Bilhões restantes. '
                                'Isso nos leva a seguinte reflexão, todo esse consumo de recursos naturais, foi sem sombra de dúvidas necessário para o desenvolvimento humano, e se não tomarmos cuidado esse recurso finito irá se esgotar, no entanto é possível que países subdesenvolvidos e em desenvolvimento, consigam crescer e competir com países que tiveram tempo para usufruir desses recursos sem se importar com o tamanho do consumo? '
                                'Para ponderarmos sobre essa pergunta trouxemos dados sobre o desflorestamento no nível continental, passando por países desenvolvidos do continente europeu, e por ultimo trazendo para algumas regiões do brasil, para uma comparação em escala reduzida a algumas décadas. '
                            )
                        ])
                    ], id="texto"),
                ],md=7),
            ]),

            html.Div([ 
                html.Br(),  ## Quebra de linha
                html.Br()
            ]),
            dbc.Row([
                    html.Div([ ## Botões
                        dbc.Button("Geral", color="primary", id="but-geral", size="lg", n_clicks=0),
                        dbc.Button("América do Norte", color="primary", id="but-america", size="lg", n_clicks=0),
                        dbc.Button("Brasil", color="primary", id="but-brasil", size="lg", n_clicks=0),
                        dbc.Button("Europa", color="primary", id="but-europa", size="lg", n_clicks=0),
                    ], id="b1"),
                    
            ]),
            html.Div([
                html.Br()
            ]),
            dbc.Row([
                dbc.Col([
                    dbc.Row ([      ##Dropdown
                        dbc.Col ([
                            html.P("Selecione o local de foco de queimadas:"),
                            dcc.Dropdown(id="drop1",
                                options=[{"label": j, "value": i} for i, j in opcoes.items()], #j recebe a chave do dicicionário e j recebe o valor
                                style={"margin-top": "10px"},
                                clearable=True
                                ),                        
                        ]),
                        dbc.Col ([
                            html.P("Selecione o ano:"),
                            dcc.Dropdown(id="drop2",
                            options=[{"label": j, "value": i} for i, j in anos.items()], #j recebe a chave do dicicionário e j recebe o valor
                            style={"margin-top": "10px"},
                            clearable=True
                            ),                        
                        ],), 
                    ]),              
                    html.Div([
                        dcc.Graph(id="graph1", style={"height":"50vh"})
                    ]),
                ],md=6),
                dbc.Col([
                    html.Div([
                        html.Br(),
                        html.Br(),
                        html.Br()
                    ]),
                    dcc.Loading(children=[

                        dcc.Graph(id="graph2", style={"height": "50vh", "margin-right": "10px", "bottom":"400px"})
                        ])

                ],md=6),

            ], id = "corpo2"),
            dbc.Row([
                html.Div([
                    html.H1("teste")
                ])
            ], id="final"),
        ], id="pai2"),
fluid=True, id="pai1")

############# Callback

    #Foi necessário colocar global em algumas variáveis, pois acusava erro de escopo

@app.callback( ## Toda vez que clicar em algum dos botões, o dropdown é redefinido ; as opções estão armazenadas em country1 e opcoes assume o valor ao clicar em algum botão
    Output('drop1', 'options'),
    Input('but-brasil', 'n_clicks'), Input('but-geral', 'n_clicks'), Input('but-europa', 'n_clicks'), Input('but-america', 'n_clicks'))
def butsgeral(bras, geral, euro, eua):
    global opcoes #opcoes é um dicionário vazio que vai receber valores de acordo com o botão a ser clicado, o global é pra não dar erro de escopo
    changed_id = [p['prop_id'] for p in callback_context.triggered][0] #atualiza a callback caso outro botão seja clicado
    if 'but-brasil' in changed_id:
        opcoes = brasil1    #brasil1, geral1, euro1, america1 são dicionários definidos anteriormente
    if 'but-geral' in changed_id:
        opcoes = geral1
    if 'but-europa' in changed_id:
        opcoes = euro1
    if 'but-america' in changed_id:
        opcoes = america1
    return opcoes
   

@app.callback( #essa callback considera a opção escolhida no primeiro select, e manda pro segundo select opções de anos de acordo com o primeiro select
    Output('drop2', 'options'),
    Input('drop1', 'value'))
def define_ano(year):
    global anos #anos é um dicionário vazio, o global é pra não dar erro de escopo
    if year == "Desmatamento no Cerrado":
        anos = brasil_ce #anos recebe uma lista de opções definidas em brasil_ce
    if year == "Desmatamento na Amazônia":
        anos = brasil_am
    if year == "Desmatamento na Europa":
        anos = {} #retorna uma lista de opções vazia, pois não há ano para selecionar
    if year == "Desmatamento no Mundo":
        anos = {}
    return anos

@app.callback ( #o primeiro gráfico é atualizado de acordo com as opções escolhidas no select 1  e 2
    Output('graph1', 'figure'),
    Input('drop2', 'value'), Input('drop1', 'value'), Input('drop1', 'value'), Input('drop1', 'value'), Input('drop1', 'value'))
def cerrado(ano_select, cerra, amaz, europ, geral):
    global c3
    global c1 #global pra não dar erro de escopo, c1,c2 e c3 são arrays vazias que vão armazenar os dados do ano, desmatamento e local de cada tabela
    global c2
        #No Mundo
    if geral == "Desmatamento no Mundo": ## Se o select1 for igual a Desmatamento no Mundo, essa condição retorna um gráfico
        fig = px.bar(tabela_array, x = 0, y = 2, color = 1, barmode='group',
             labels = {'0': 'Continente', '1' :'Ano', '2':'Desmatamento'},
             title = 'Perca de áreas florestais por continente')
        fig.update_layout(paper_bgcolor = '#242424', plot_bgcolor = '#242424', title_font_family = 'Courier New', title = 'Perda de área florestal por hectares',font_color = 'white'), 
        return fig
        #Na Europa
    if europ == "Desmatamento na Europa":
        fig = px.bar(vetor1, x=1, y=2, color= 0, 
             labels= {'0':"Países",'1':"Ano", '2':"Área Desmatada em Hectares"},
             )
        fig.update_layout(
            font_color = 'white',
            paper_bgcolor="#242424", 
            plot_bgcolor="#242424",
            title="Desmatamento na Europa(2000-2020)",
        )
        return fig
        ## Na Amazônia
    if ano_select == "2013" and amaz == "Desmatamento na Amazônia":
        c2 = dk[dk['Ano'] == 2013]
        c1 = c2['Estado']
        c3 = c2['qnt']
    if ano_select == "2012" and amaz == "Desmatamento na Amazônia":
        c2 = dk[dk['Ano'] == 2012]
        c1 = c2['Estado']
        c3 = c2['qnt']
    if ano_select == "2011" and amaz == "Desmatamento na Amazônia":
        c2 = dk[dk['Ano'] == 2011]
        c1 = c2['Estado']
        c3 = c2['qnt']
    if ano_select == "2010" and amaz == "Desmatamento na Amazônia":
        c2 = dk[dk['Ano'] == 2010]
        c1 = c2['Estado']
        c3 = c2['qnt']
    if ano_select == "2009" and amaz == "Desmatamento na Amazônia":
        c2 = dk[dk['Ano'] == 2009]
        c1 = c2['Estado']
        c3 = c2['qnt']
    if ano_select == "2008" and amaz == "Desmatamento na Amazônia":
        c2 = dk[dk['Ano'] == 2008]
        c1 = c2['Estado']
        c3 = c2['qnt']
    if ano_select == "2007" and amaz == "Desmatamento na Amazônia":
        c2 = dk[dk['Ano'] == 2007]
        c1 = c2['Estado']
        c3 = c2['qnt']
    if ano_select == "2006" and amaz == "Desmatamento na Amazônia":
        c2 = dk[dk['Ano'] == 2006]
        c1 = c2['Estado']
        c3 = c2['qnt']
    if ano_select == "2005" and amaz == "Desmatamento na Amazônia":
        c2 = dk[dk['Ano'] == 2005]
        c1 = c2['Estado']
        c3 = c2['qnt']
    if ano_select == "2004" and amaz == "Desmatamento na Amazônia":
        c2 = dk[dk['Ano'] == 2004]
        c1 = c2['Estado']
        c3 = c2['qnt']
    if ano_select == "2003" and amaz == "Desmatamento na Amazônia":
        c2 = dk[dk['Ano'] == 2003]
        c1 = c2['Estado']
        c3 = c2['qnt']
    if ano_select == "2002" and amaz == "Desmatamento na Amazônia":
        c2 = dk[dk['Ano'] == 2002]
        c1 = c2['Estado']
        c3 = c2['qnt']
    if ano_select == "2001" and amaz == "Desmatamento na Amazônia":
        c2 = dk[dk['Ano'] == 2001]
        c1 = c2['Estado']
        c3 = c2['qnt']
    if ano_select == "2000" and amaz == "Desmatamento na Amazônia":
        c2 = dk[dk['Ano'] == 2000]
        c1 = c2['Estado']
        c3 = c2['qnt']
    if ano_select == "1999" and amaz == "Desmatamento na Amazônia":
        c2 = dk[dk['Ano'] == 1999]
        c1 = c2['Estado']
        c3 = c2['qnt']
    if ano_select == "1998" and amaz == "Desmatamento na Amazônia":
        c2 = dk[dk['Ano'] == 1998]
        c1 = c2['Estado']
        c3 = c2['qnt']
        ## No cerrado
    if ano_select == "2021" and cerra == "Desmatamento no Cerrado":
        c3 = v2 #v2 foi definido anteriormente
        c1 =v1 #v1 foi definido anteriormente, armazena os estados do gráfico do cerrado
    if ano_select == "2020" and cerra == "Desmatamento no Cerrado":
        c3 = v3
        c1 =v1
    if ano_select == "2019" and cerra == "Desmatamento no Cerrado":
        c3 = v4
        c1 =v1
    if ano_select == "todos os anos" and cerra == "Desmatamento no Cerrado":
        c3 = v4 + v3 + v2
        c1 =v1 
    fig = go.Figure()
    fig.add_trace(go.Bar(
                x=c1,
                y=c3,
                name='Gráfico 1',
                marker_color='#389fd6'   
                ))
    fig.update_layout(barmode='group', xaxis_tickangle=-45, font_color = 'white', paper_bgcolor="#242424", 
            plot_bgcolor="#242424", title="Área de Desmatamento", xaxis_title="Estado", yaxis_title="Área Desmatada (Km2)"
                    )
    return fig

@app.callback ( #callback do segundo mapa, leva em consideração os valores selecionados em select1 e select2,
    Output('graph2', 'figure'),
    Input('drop2', 'value'), Input('drop1', 'value'), Input('drop1', 'value'), Input('drop1', 'value'), Input('drop1', 'value'))
def amazonia(ano_selects, cerra, amaz, europ, conti):
    global ns
        ## Na europa
    if europ == "Desmatamento na Europa": #verifica se a opção no select 1 para passar as próximas variáveis pro mapa
        xs = df  #xs definide o dataframe para o gráfico do mapa
        xt = "Forest Area Change" #xt define o valor do dado a ser analisado (área de desmatamento e etc)
        xp = "Country" #xp define o local no mapa, estados, continentes, países
        lt, ln = 58.46, 15.59 #define latitude e longitude no mapa
        
        ## Na amazônia
    if ano_selects == "2014" and amaz == "Desmatamento na Amazônia":
        xs = dk[dk['Ano'] == 2014]
        xt = "qnt"
        xp = "Estado"
        lt, ln = -16.95, -47.78
    if ano_selects == "2013" and amaz == "Desmatamento na Amazônia":
        xs = dk[dk['Ano'] == 2013]
        xt = "qnt"
        xp = "Estado"
        lt, ln = -16.95, -47.78
    if ano_selects == "2012" and amaz == "Desmatamento na Amazônia":
        xs = dk[dk['Ano'] == 2012]
        xt = "qnt"
        xp = "Estado"
        lt, ln = -16.95, -47.78
    if ano_selects == "2011" and amaz == "Desmatamento na Amazônia":
        xs = dk[dk['Ano'] == 2011]
        xt = "qnt"
        xp = "Estado"
        lt, ln = -16.95, -47.78
    if ano_selects == "2010" and amaz == "Desmatamento na Amazônia":
        xs = dk[dk['Ano'] == 2010]
        xt = "qnt"
        xp = "Estado"
        lt, ln = -16.95, -47.78
    if ano_selects == "2009" and amaz == "Desmatamento na Amazônia":
        xs = dk[dk['Ano'] == 2009]
        xt = "qnt"
        xp = "Estado"
        lt, ln = -16.95, -47.78
    if ano_selects == "2008" and amaz == "Desmatamento na Amazônia":
        xs = dk[dk['Ano'] == 2008]
        xt = "qnt"
        xp = "Estado"
        lt, ln = -16.95, -47.78
    if ano_selects == "2007" and amaz == "Desmatamento na Amazônia":
        xs = dk[dk['Ano'] == 2007]
        xt = "qnt"
        xp = "Estado"
        lt, ln = -16.95, -47.78
    if ano_selects == "2006" and amaz == "Desmatamento na Amazônia":
        xs = dk[dk['Ano'] == 2006]
        xt = "qnt"
        xp = "Estado"
        lt, ln = -16.95, -47.78
    if ano_selects == "2005" and amaz == "Desmatamento na Amazônia":
        xs = dk[dk['Ano'] == 2005]
        xt = "qnt"
        xp = "Estado"
        lt, ln = -16.95, -47.78
    if ano_selects == "2004" and amaz == "Desmatamento na Amazônia":
        xs = dk[dk['Ano'] == 2004]
        xt = "qnt"
        xp = "Estado"
        lt, ln = -16.95, -47.78
    if ano_selects == "2003" and amaz == "Desmatamento na Amazônia":
        xs = dk[dk['Ano'] == 2003]
        xt = "qnt"
        xp = "Estado"
        lt, ln = -16.95, -47.78
    if ano_selects == "2002" and amaz == "Desmatamento na Amazônia":
        xs = dk[dk['Ano'] == 2002]
        xt = "qnt"
        xp = "Estado"
        lt, ln = -16.95, -47.78
    if ano_selects == "2001" and amaz == "Desmatamento na Amazônia":
        xs = dk[dk['Ano'] == 2001]
        xt = "qnt"
        xp = "Estado"
        lt, ln = -16.95, -47.78
    if ano_selects == "2000" and amaz == "Desmatamento na Amazônia":
        xs = dk[dk['Ano'] == 2000]
        xt = "qnt"
        xp = "Estado"
        lt, ln = -16.95, -47.78
    if ano_selects == "1999" and amaz == "Desmatamento na Amazônia":
        xs = dk[dk['Ano'] == 1999]
        xt = "qnt"
        xp = "Estado"
        lt, ln = -16.95, -47.78
    if ano_selects == "1998" and amaz == "Desmatamento na Amazônia":
        xs = dk[dk['Ano'] == 1998]
        xt = "qnt"    
        xp = "Estado"  
        lt, ln = -16.95, -47.78     
            ## No Cerrado    
    if ano_selects == "2021" and cerra == "Desmatamento no Cerrado":
        ns = 2021
        xs = dt[dt['Ano'] == ns]
        xt = "Área (Km2)"
        xp = "Estado"
        lt, ln = -16.95, -47.78
    if ano_selects == "2020" and cerra == "Desmatamento no Cerrado":
        ns = 2020
        xs = dt[dt['Ano'] == ns]
        xt = "Área (Km2)"
        xp = "Estado"
        lt, ln = -16.95, -47.78
    if ano_selects == "2019" and cerra == "Desmatamento no Cerrado":
        ns = 2019
        xs = dt[dt['Ano'] == ns]
        xt = "Área (Km2)"
        xp = "Estado"
        lt, ln = -16.95, -47.78
        ## NO MUNDO
    if conti == "Desmatamento no Mundo": 
        xt = "Desmatamento"
        xp = "Continentes"  
        lt, ln = 31.58, 119.77
        xs = dn


    fig2 = px.choropleth_mapbox(xs, locations=xp, color=xt,
                        center={"lat": lt, "lon": ln}, zoom=3.2,
                            geojson=maps, color_continuous_scale="PuBu", opacity=0.4,
                        )
    fig2.update_layout(
        paper_bgcolor="#242424", 
        autosize=True, 
        margin = go.Margin(l=0, r=0, t=0, b=0),
        showlegend = False,
        mapbox_style="carto-darkmatter",
        font_color = 'white'
    )



    return fig2





if __name__ == '__main__':
    app.run_server(debug=True)


