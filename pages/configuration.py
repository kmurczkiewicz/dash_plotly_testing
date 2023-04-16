import dash
import dash_bootstrap_components as dbc

dash.register_page(__name__, path='/')

content = dash.html.Div(
    id="page-content",
    children=[
        dash.html.H1(children='Configuration',  className="text-primary text-center fs-3")
    ]
)

layout = dash.html.Div(children=[
    content,
    #sidebar,
])