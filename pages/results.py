import dash

dash.register_page(__name__, path='/results')

layout = dash.html.Div(children=[
    dash.html.H1(children='Results',  className="text-primary text-center fs-3")
])