# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 11:37:12 2017

@author: rjr
"""

import bs4 as bs
import pickle
import requests
import datetime as dt
import os
import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np

style.use("ggplot")

def saveSP500():
    """Function to save tickers from the S&P 500
    
    Retrieves the 500 S&P tickers from wikipedia via BeautifulSoup and places
    them in a list.
    
    Args:
        Takes zero arguments
    
    Returns:
        A list with the tickers
        
    Raises:
        N/A
    """
    
    response = requests.get("https://en.wikipedia.org/wiki/List_of_S%26P_500_companies")
    soup = bs.BeautifulSoup(response.text, "lxml")
    table = soup.find("table", {"class":"wikitable sortable"})
    tickers = []
    
    for row in table.findAll("tr")[1:]:
        ticker = row.findAll("td")[0].text
        ticker = ticker.replace('.','-').strip()
        tickers.append(ticker)
        print(ticker)
    
    with open("sp500tickers.pickle", "wb") as f:
        pickle.dump(tickers, f)
        
    print(tickers)
    return tickers

def getYahooData(reloadsaveSP500 = False):
    try:
        if reloadsaveSP500 == True:
            tickers = saveSP500()
        else:
            with open("sp500tickers.pickle", "rb") as f:
                tickers = pickle.load(f)
        
        if not os.path.exists("stockDFs"):
            os.makedirs("stockDFs")
            
        start = dt.datetime(2000, 1, 1)
        end = dt.datetime(2017, 12, 10)
        
        for ticker in tickers:
            print(ticker)
            if not os.path.exists("StockDFs/{}.csv".format(ticker)):
                df = web.DataReader(ticker, "yahoo", start, end)
                df.to_csv("StockDFs/{}.csv".format(ticker))
            else:
                print("ALready have {}".format(ticker))
    except:
        print("trying again")
        for i in range(0, 10):
            getYahooData()


def compileData():
    with open("sp500tickers.pickle", "rb") as f:
        tickers = pickle.load(f)
        
    mainDF = pd.DataFrame()
    
    for count, ticker in enumerate(tickers):
        df = pd.read_csv("stockDFs/{}.csv".format(ticker))
        df.set_index("Date", inplace = True)
        
        df.rename(columns = {"Adj Close": ticker}, inplace = True)
        df.drop(["Open", "High", "Low", "Close", "Volume"], 1, inplace = True)
        
        if mainDF.empty:
            mainDF = df
        else:
            mainDF = mainDF.join(df, how = "outer")
            
        if count % 10 == 0:
            print(count)
    print(mainDF.head())
    mainDF.to_csv("SP500JoinedToCSV.csv")
    
def visualizeData():
    df = pd.read_csv("SP500JoinedToCSV.csv")
    dfCorr = df.corr()
    
    data = dfCorr.values
    fig = plt.figure()
    
    ax = fig.add_subplot(1, 1, 1)
    
    heatmap = ax.pcolor(data, cmap = plt.cm.RdYlGn)
    fig.colorbar(heatmap)
    ax.set_xticks(np.arange(data.shape[0]) + 0.5, minor = False)
    ax.set_yticks(np.arange(data.shape[1]) + 0.5, minor = False)
    ax.invert_yaxis()
    ax.xaxis.tick_top()
    
    columnLabels = dfCorr.columns
    rowLabels = dfCorr.index
    
    ax.set_xticklabels(columnLabels)
    ax.set_yticklabels(rowLabels)
    plt.xticks(rotation = 90)
    heatmap.set_clim(-1, 1)
    plt.tight_layout()
    plt.show()
    
    
    
    
saveSP500()
            
        