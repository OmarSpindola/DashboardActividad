import dash 
from dash import dcc
from dash import html
import plotly
import plotly.express as px
import pandas as pd
from graph import get_graph1
from graph import get_graph2

app = dash.Dash()

app.layout = html.Div([
    html.H1("Actividad: Dashboard 1 Dash", style={"textAlign":'center'}),
    html.H3("Paloma Pardo"),
    html.H3("Omar Spíndola"),
    html.H3("Martín Guzmán"),
    html.H3("Santiago Peña"),
    html.H3("Ricardo Álvarez"),
    html.P("A continuación presentaremos dos gráficos de nuestro proyecto creados con plotly."),
    dcc.Graph(id="graph1", figure = get_graph1()),
    dcc.Graph(id="graph2", figure = get_graph2())])

if __name__ == "__main__":
    app.run_server()
