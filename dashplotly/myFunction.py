
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import seaborn as sns
import plotly.graph_objs as go
from dash.dependencies import Input, Output
import numpy as np
from sqlalchemy import create_engine


def getDataframe(query):
    query = conn.execute(query).fetchall()
    dataframe = pd.DataFrame(query)
    dataframe.columns = query[0].keys()
    dataframe.set_index('id', inplace=True)

    return dataframe

goList = {
    'bar': go.Bar,
    'violin': go.Violin,
    'box': go.Box
}

def getPlot(x, jenisGo):
    return [
            goList[jenisGo] (
                x = titanicDF[x],
                y = titanicDF['fare'],
                text = titanicDF['fare'],
                opacity=0.7,
                name='Fare',
                legendgroup='Fare',
                marker=dict(color='blue')
            ),
            goList[jenisGo] (
                x = titanicDF[x],
                y = titanicDF['age'],
                text = titanicDF['age'],
                opacity=0.7,
                name='Age',
                legendgroup='Age',
                marker=dict(color='orange')
            ),
        ]  

# connect db
engine = create_engine("mysql+mysqlconnector://root:@localhost/ujiantitanic?host=localhost?port=3306")
conn = engine.connect()
titanicDF = getDataframe("SELECT * FROM titanic")
titanicOutDF = getDataframe("SELECT * FROM titanicoutcalc")

