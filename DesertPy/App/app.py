# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 19:13:29 2018

@author: rjr
"""

# Desertpy 04/10/2018 notes: Introduction to Dash
# Creating a simple app w/ Dash

import dash
import dash_html_components as html
import dash_core_components as dcc

def load_df():
    '''
    Returns a pandas df of the iris dataset
    '''
    data = datasets.load_iris().data
    cols = datasets.load_iris().feature_names
    df = pd.DataFrame(data=data, columns=cols)
    df['target'] = datasets.load_iris().target
    return df
    

app = dash.Dash()
df = load_df()


app.layout = html.Div([
        html.H2("Iris Visualization")
        ])



if __name__ == "__main__":
    app.run_server(debug=True)