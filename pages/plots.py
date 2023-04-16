import dash

dash.register_page(__name__, path='/plots')

layout = dash.html.Div(children=[
    dash.html.H1(children='Plots',  className="text-primary text-center fs-3")
])