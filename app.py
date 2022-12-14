# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import gunicorn
from whitenoise import WhiteNoise


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

server.wsgi_app = WhiteNoise(server.wsgi_app, root='static/') 


df = pd.read_json("https://data.usaid.gov/resource/a3rc-nmf6.json")

fig_country_value = px.histogram(df, x="country", y=["line_item_value"],
        barmode="stack", title='2020 Line Item Costs by Country ($)',
        text_auto='.1s', template='plotly_dark')
fig_country_value.update_layout(xaxis={'categoryorder':'total descending'})
fig_country_value.update_layout(showlegend=False)

fig_molecule_type = px.histogram(df, x="molecule_test_type", y=["line_item_value"],
        barmode="stack", title='2020 Line Item Costs by Molecule Test Type ($)',
        text_auto='.1s', template='plotly_dark')
fig_molecule_type.update_layout(xaxis={'categoryorder':'total descending'})
fig_molecule_type.update_layout(showlegend=False)


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
        figure= fig_country_value
    ),
    dcc.Graph(
        id='value of shipments by molecule type',
        figure=fig_molecule_type
    )
])

if __name__ == "__main__": app.run_server(debug=False, host='0.0.0.0', port=8050)