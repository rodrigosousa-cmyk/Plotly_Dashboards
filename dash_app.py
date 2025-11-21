# This code Requires Dash 2.17.0 or later
from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

# load dataset
df = px.data.gapminder()

# start app
app = Dash()

# set page layout
app.layout = [
    html.H1(children='Title of Dash App', style={'textAlign':'center'}),
    dcc.Dropdown(df.continent.unique(), 'Asia' , id='dropdown-selection'),
    dcc.Graph(id='graph-content')
]
#
@callback(
    Output('graph-content', 'figure'),
    # select indicators
    Input('dropdown-selection', 'value'))
#
def update_graph(value):
    figure = px.scatter(df, x="gdpPercap", y="lifeExp", animation_frame="year",
         animation_group="country", size="pop", color="continent",
         hover_name="country", log_x=True, size_max=60,
         range_x=[100, 100000], range_y=[25, 90])
    return figure.show()
#
if __name__ == '__main__':
    app.run(debug=False)
