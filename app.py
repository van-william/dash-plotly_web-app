# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
#import gunicorn
#from whitenoise import WhiteNoise


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

#server.wsgi_app = WhiteNoise(server.wsgi_app, root='static/') 

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.read_json("https://data.usaid.gov/resource/a3rc-nmf6.json")

fig = px.histogram(df, x="country", y=["line_item_value"],
        barmode="stack", title='2020 Line Item Costs by Country',
        text_auto='.1s')

fig.update_layout(xaxis={'categoryorder':'total descending'})
fig.update_layout(showlegend=False)
app.layout = html.Div(children=[
    html.H1(children='USAID Summary Dashboard 2020'),
    html.H2(children='''
    Experimental Web App on Dash for Visualizing USAID Data.
    '''),
    html.H2(children='''
    Doby. 2020. Supply Chain Shipment Pricing Data. Dataset. USAID Development Data Library. https://data.usaid.gov/d/a3rc-nmf6.
    '''),

    dcc.Graph(
        id='value of shipments by country',
        figure= fig

    )
])

if __name__ == "__main__": app.run_server(debug=False, host='0.0.0.0', port=8050)