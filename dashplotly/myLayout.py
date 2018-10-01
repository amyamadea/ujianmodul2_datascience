
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
from myFunction import titanicDF, titanicOutDF

app = dash.Dash()
app.title = 'Latihan Ujian'

app.layout = html.Div(
    children=[
        dcc.Tabs(id='tabs', value='tab-1', 
            children=[
                dcc.Tab(label='Ujian Titanic Database', value='tab-1', children=[
                    html.Div([
                        html.Table([
                            html.Tr([
                                html.Td([html.P('Table: ')]),
                                html.Td([
                                    dcc.Dropdown(
                                        id='ddl-table-tab1',
                                        options=[
                                            {'label': 'Titanic', 'value': 'titanicDF'},
                                            {'label': 'Titanic Outlier', 'value': 'titanicOutDF'}
                                        ],
                                        value='titanicDF'
                                    ),
                                ]),
                            ])
                        ], style = {'width' : '800px'}),
                        dcc.Graph(
                            id='tbl-titanic-tab1',
                            figure = { 
                                'data': [],
                                'layout' : go.Layout(
                                    height=600, margin={'t': 10}, width=900
                                )
                            }
                        ),
                    ])
                ]),
                dcc.Tab(label='Product Histogram', value='tab-2', children=[
                    html.Div([
                        html.Table([
                            html.Tr([
                                html.Td([html.P('Jenis: ')]),
                                html.Td([
                                    dcc.Dropdown(
                                        id='ddl-jenis-tab2',
                                        options=[
                                            {'label': 'Bar', 'value': 'bar'},
                                            {'label': 'Violin', 'value': 'violin'},
                                            {'label': 'Box', 'value': 'box'},
                                        ],
                                        value='bar'
                                    ),
                                ]),
                            ]),
                            html.Tr([
                                html.Td([html.P('X Axis: ')]),
                                html.Td([
                                    dcc.Dropdown(
                                        id='ddl-xaxis-tab2',
                                        options=[
                                            {'label': 'Survived', 'value': 'survived'},
                                            {'label': 'Sex', 'value': 'sex'},
                                            {'label': 'Ticket Class', 'value': 'class'},
                                            {'label': 'Who', 'value': 'who'},
                                            {'label': 'Outlier', 'value': 'outlier'},
                                        ],
                                        value='survived'
                                    ),
                                ]),
                            ])
                        ], style = {'width' : '400px'}),
                        dcc.Graph(
                            id='graph-tab2',
                            figure={ # kanvas
                                'data': [],
                                'layout' : go.Layout(
                                    xaxis = {'title' : 'Data Titanic'},
                                    yaxis = {'title' : 'Count'},
                                    margin = {'l': 40, 'b': 40, 't':40, 'r':10},
                                    hovermode = 'closest',
                                    # legend={'x':0, 'y':1} # menentukan lokasi legend,
                                    boxmode = 'group', violinmode = 'group' # agar violin dan box terpisah
                                )
                            }
                        )
                    ])
                ])
            ],
            style = { # untuk tab
                'fontFamily' : 'system-ui'
            },
            content_style = { # untuk conten yg dibungkus tab
                'fontFamily' : 'Calibri',
                'borderLeft' : '1px solid #d6d6d6',
                'borderRight' : '1px solid #d6d6d6',
                'borderBottom' : '1px solid #d6d6d6',
                'padding' : '40px'
            },
        ),
    ],
    style = {
            'maxWidth' : '1000px',
            'margin' : '0 auto'
        }
)