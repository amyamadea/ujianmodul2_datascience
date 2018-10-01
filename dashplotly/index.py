
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import seaborn as sns
import plotly.graph_objs as go
from dash.dependencies import Input, Output
import numpy as np
from sqlalchemy import create_engine

import myFunction
from myFunction import titanicDF, titanicOutDF, getPlot

import myLayout
from myLayout import app

@app.callback(
    Output('tbl-titanic-tab1', 'figure'), 
    [Input('ddl-table-tab1', 'value')]
)
def set_titanic_table_tab1(table):
    if (table=='titanicDF'):
        df = titanicDF
    else:
        df = titanicOutDF
    return { 
        'data': [
            go.Table(
                header=dict(values=list(df.columns),
                    fill = dict(color='#C2D4FF'),
                    align = ['center'] * 5
                ),  
                cells=dict(values=[df[col] for col in df.columns], align=['left'])
            )
        ],
        'layout' : go.Layout(
            height=600, margin={'t': 10}, width=900
        )
    }

@app.callback(
    Output('graph-tab2', 'figure'), 
    [Input('ddl-jenis-tab2', 'value'), Input('ddl-xaxis-tab2', 'value')]
)
def updateCategoryGraph(jenisplot, x):
    return {
        'data' : getPlot(x, jenisplot),
        'layout' : 
            go.Layout(
                xaxis = {'title' : x.capitalize()},
                yaxis = {'title' : 'Count'},
                margin = {'l': 40, 'b': 40, 't':40, 'r':10},
                hovermode = 'closest',
                # legend={'x':0, 'y':1} # menentukan lokasi legend,
                boxmode = 'group', violinmode = 'group' # agar violin dan box terpisah
            )
    }
    

if __name__ == '__main__': # menandakan file yg di run adalah main file. tidak diimport
    # debug = True for auto restart if ode edited
    app.run_server(debug=True, port = 2828)