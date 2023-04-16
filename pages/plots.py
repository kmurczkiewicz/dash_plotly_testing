# https://stackoverflow.com/questions/55822042/how-to-draw-a-multiple-line-chart-using-plotly-express

import dash
import pandas as pd
import plotly.express as px 

pd.options.plotting.backend = "plotly"

dash.register_page(__name__, path='/plots')

@dash.callback(
    dash.Output("current_config_plot", "children"),
    dash.Input("main_store", "data"),
)
def update(main_store):
    if main_store == {}:
        return "Select config..."
    csv_to_read = "..\\" + main_store.get('selected_config') + ".csv"
    df = pd.read_csv(csv_to_read)
    fig = px.line(df, x='time',y='result', color="model")
    return dash.dcc.Graph(figure=fig)

layout = dash.html.Div(children=[
    dash.html.H1(children='Plots',  className="text-primary text-center fs-3"),
    dash.html.Div(
        id="current_config_plot",
        style={"margin-left":"20%"}
    )
])