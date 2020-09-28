from NBAFlaskApp import app
import plotly.express as px
import pandas as pd
import dash_core_components as dcc
from dash.dependencies import Input, Output
import dash
import dash_html_components as html
from flask import redirect

statsToNotBeGraphed = ['Player', 'Pos', 'Age', 'Tm', 'G', 'GS', 'MP']


def create_dropdown_dict(df):
    column_names = list(df.columns.values.tolist())
    option_list = []
    for name in column_names[5:]:
        if name not in statsToNotBeGraphed:
            option_list.append({"label": name, "value": name})

    return option_list


dash_app = dash.Dash(
    __name__,
    server=app,
    routes_pathname_prefix='/dash/'
)


df_per_game = pd.read_csv("NBA_CSV_Files/NBA_PLAYER_STATS_2019-2020")
df_advanced = pd.read_csv("NBA_CSV_Files/NBA_ADVANCED_PLAYER_STATS_2019-2020")


dash_app.layout = html.Div([
    html.H1("NBA Stat Dashboard Using Dash", style={'text-align': 'center'}),

    html.Div([
        html.H4("Select X variable."),
        dcc.Dropdown(id="x_var",
                     options=create_dropdown_dict(df_per_game),
                     multi=False,
                     value="FG%",
                     style={'width': "40%"}
                     )
        ]),
    html.Div([
        html.H4("Select Y variable."),
        dcc.Dropdown(id="y_var",
                     options=create_dropdown_dict(df_per_game),
                     multi=False,
                     value="STL",
                     style={'width': "40%"}
                     ),

    ]),

    html.Div(id='output_container', children=[]),
    html.Br(),


    dcc.Graph(id="stat_map", figure={})
])


@dash_app.callback(
    Output("stat_map", 'figure'),
    [Input(component_id="x_var", component_property="value"),
     Input(component_id="y_var", component_property="value")]
)
def update_graph(x_var, y_var):
    print(x_var)
    print(type(x_var))
    print(y_var)
    print(type(y_var))

    dff_per_game = df_per_game.copy()

    # list_x = dff_per_game[x_var].tolist()
    # list_y = dff_per_game[y_var].tolist()
    #
    # print(list_x)
    # print(list_y)

    fig = px.scatter(
        data_frame=dff_per_game,
        x=x_var,

        y=y_var,
        size='G',
        hover_data=["Player"]
    )
    return fig



@app.route('/test')
def test():
    print(create_dropdown_dict(df_per_game))
    return redirect('/dash/')



