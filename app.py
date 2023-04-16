# https://github.com/AnnMarieW/dash-multi-page-app-demos

import dash
import dash_bootstrap_components as dbc

external_stylesheets = [dbc.themes.CERULEAN]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets, use_pages=True)

SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}


sidebar = dash.html.Div(
    [
        dash.html.H2("Menu", className="display-4"),
        dash.html.Hr(),
        dash.html.P(
            "Navigation", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink(f"{page['name']}", href=page["relative_path"], active=False)
                for page in dash.page_registry.values()
            ],
            vertical=True,
            pills=True,
        ),
        dash.html.Hr(),
        dash.html.P(
            "Configuration", className="lead"
        ),
        dbc.Nav(
            [
                dash.dcc.Dropdown(["ww03", "ww02", "ww01"], "ww03", id="configs", clearable=False, persistence="session"),
            ],
            vertical=True,
            pills=True,
        ),

    ],
    style=SIDEBAR_STYLE,
)

app.layout = dash.html.Div([
    dash.dcc.Store(id='main_store', data={}),
	sidebar,
    dash.html.H1('Test dashboard', className="text-primary text-center fs-3"),
    dash.html.H3(id='my-output', className="text-primary text-center fs-3"),
	dash.page_container
])

### Callbacks
@app.callback(
    dash.Output(component_id='main_store', component_property='data'),
    dash.Input(component_id='configs', component_property='value')
)
def update_output(value):
    return {
        "selected_config" : value
    }


# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)


