import dash
import dash_bootstrap_components as dbc

dash.register_page(__name__, path='/')

@dash.callback(
    dash.Output("current_config", "children"),
    dash.Input("main_store", "data"),
)
def update(main_store):
    if main_store == {}:
        return "Select config..."
    return f"Selected config: {main_store.get('selected_config')}"

content = dash.html.Div(
    id="page-content",
    children=[
        dash.html.H1(children='Configuration',  className="text-primary text-center fs-3"),
        dash.html.Div(id="current_config", className="text-primary text-center fs-3")
    ]
)

layout = dash.html.Div(children=[
    content,
])

