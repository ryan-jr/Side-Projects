# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 04:40:25 2017

@author: rjr
"""



import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
from matplotlib.finance import candlestick_ohlc
import matplotlib.dates as mdates
import pandas as pd
import pandas_datareader.data as web

# Set the style/initialize vars
"""
style.use("ggplot")
start =dt.datetime(2000, 1, 1)
end =dt.datetime(2016, 12, 31)
df = web.DataReader("TSLA", "yahoo", start, end)
df.to_csv("TSLA.csv")
"""

df = pd.read_csv("TSLA.csv", parse_dates = True, index_col = 0)
#df["100MA"] = df["Adj Close"].rolling(window = 100).mean()


dfOhlc = df["Adj Close"].resample("10D").ohlc()
dfVolume = df["Volume"].resample("10D").sum()
dfOhlc.reset_index(inplace = True)

dfOhlc["Date"] = dfOhlc["Date"].map(mdates.date2num)
print(dfOhlc.head())


# Multiple graphs together in MPL are refered to as axis, hence the var name
# SPec grid size, starting point
ax1 = plt.subplot2grid((6, 1), (0, 0), rowspan = 5, colspan = 1)
ax2 = plt.subplot2grid((6, 1), (5, 0), rowspan = 1, colspan = 1)
ax1.xaxis_date()

candlestick_ohlc(ax1, dfOhlc.values, width = 2, colorup = "g")
ax2.fill_between(dfVolume.index.map(mdates.date2num), dfVolume.values, 0)



