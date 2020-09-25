import yfinance as yf
import os
import datetime
import pandas as pd
import numpy as np

today = datetime.datetime.now()

f = open("symbolfetcher/symbolList.txt", "r")
symbols = []
for name in f:
    symbols.append(name[:-1])
newlist = symbols
tick = yf.Ticker(newlist[0])
hist = tick.history(period="1d")
hist.insert(0,'Symbol',newlist[0], True)
tick2 = yf.Ticker(newlist[1])
hist2 = tick2.history(period="1d")
hist2.insert(0,'Symbol',newlist[1], True)
combined = pd.concat([hist,hist2])

for x in range(2,len(newlist)):
    tick2 = yf.Ticker(newlist[x])
    hist2 = tick2.history(period="1d")
    hist2.insert(0,'Symbol',newlist[x], True)
    combined = pd.concat([combined,hist2])

print(combined)
combined.to_csv("Incremental -" + today.strftime("%c") + ".csv")
