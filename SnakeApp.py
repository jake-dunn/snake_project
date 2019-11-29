import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import plotly.graph_objs as go
from dash.dependencies import Input, Output
from SnakeGame import SnakeGame

app = dash.Dash("Jake's Snake App")

"""
Page Contents
"""
sg = SnakeGame(20)


def plot_game():
    game = dcc.Graph(
        id="game",
        figure=go.Figure(data=go.Heatmap(
            z=sg.plot_snake(sg.grid, sg.head_val)
        ),
            layout=go.Layout(
                height=500,
                margin={"l": 60, "r": 20, "b": 20, "t": 60, "pad": 0},
            ),
        )
    )
    return game


# heading_card = dbc.Card(
#     [html.H3("Snake Game"), html.Hr()],
#     body=True,
#     style={"height": "100%"},
# )

game_board = dbc.Card(
    [
        html.H3("Board"),
        html.Hr(),
        html.Div(id="game_board", children=[]),
    ],
    body=True,
    style={"height": "100%"},
)

buttons = html.Div(
    [
        dbc.Button("Left", color="primary", id="lb"),
        dbc.Button("Right", color="primary", id="rb"),
        dbc.Button("Up", color="primary", id="ub"),
        dbc.Button("Down", color="primary", id="db"),
    ]
)


"""
Build the Page
"""

app.layout = dbc.Container(
    children=[#dbc.Row(heading_card),
              html.Br(),
              dbc.Row([game_board]),
              html.Br(),
              dbc.Row(buttons)
              ]
)

"""CallBacks"""
@app.callback(
    Output("game_board", "children"), [Input("rb", "n_clicks")]
)
def move_right(n):
    sg.move_snake('right')
    return plot_game()


if __name__ == "__main__":
    app.run_server(port=8888, debug=True)
    #
