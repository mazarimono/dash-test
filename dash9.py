import dash 
import dash_core_components as dcc 
import dash_html_components as html 
import pandas as pd 
import plotly.graph_objs as go 

df = pd.read_csv('three.csv')
df = df[['Date', 'Close**', 'name']]
df['Date'] = pd.to_datetime(df['Date'])

app = dash.Dash(__name__)

app.layout = html.Div([
                html.Div([
                    dcc.Dropdown(
                        id = 'selector',
                        options = [{'label': i, 'value': i} for i in df.name.unique()],
                        value = 'bitcoin',
                        multi = True
                        ),
                    html.Div(id = 'three-graph')
                        
                    ])
    ])

@app.callback(
    dash.dependencies.Output('three-graph', 'children'),
    [dash.dependencies.Input('selector', 'value')])
def make_chart(factors):
    graphs = []
    if not factors:
        graphs.append(html.H2(
            'Select Cryptocurrency Please!'))
    else:
        for i, factor in enumerate(factors):
            dff = df[df.name==factor]
            linechart = {
        'x': dff['Date'],
        'y': dff['Close**'],
        'type': 'Scatter',
        'name': factor,
            }

        graphs.append(dcc.Graph(
            id = factor,
        figure = {
        'data': linechart,}))

    return graphs

if __name__ == '__main__':
    app.run_server(debug=True)
