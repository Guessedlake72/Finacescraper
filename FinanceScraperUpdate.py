import yfinance as yf
import os
import os.path
from os import path
import datetime
import pandas as pd
import numpy as np

def formDate(date):
    return date.strftime("%Y") + "-" + date.strftime("%m") + "-" + date.strftime("%d")


def writeMissedCsv(daysPassed):

    startday = today - datetime.timedelta(days=daysPassed+1)
    endday = today - datetime.timedelta(days=daysPassed)
    newlist = symbols[0:10]
    tick = yf.Ticker(newlist[0])
    hist = tick.history(start=formDate(startday), end=formDate(endday))
    hist.insert(0,'Symbol',newlist[0], True)
    tick2 = yf.Ticker(newlist[1])
    hist2 = tick2.history(start=formDate(startday), end=formDate(endday))
    hist2.insert(0,'Symbol',newlist[1], True)
    combined = pd.concat([hist,hist2])

    for x in range(2,len(newlist)):
        tick2 = yf.Ticker(newlist[x])
        hist2 = tick2.history(start=formDate(startday), end=formDate(endday))
        hist2.insert(0,'Symbol',newlist[x], True)
        combined = pd.concat([combined,hist2])

    print(combined)
    combined.to_csv("Incremental -" + formDate(endday) + ".csv")

def findMissingDates(date,passed):
    print("Checking Incremental -" + formDate(date) + ".csv")
    print(path.exists("Incremental -" + formDate(date) + ".csv"))
    if path.exists("Incremental -" + formDate(date) + ".csv") or path.exists("Initial -" + formDate(date) + '/'):
        exit()
    else:
        writeMissedCsv(passed)
        findMissingDates(date - datetime.timedelta(days=1),passed+1)



f = open("symbolfetcher/symbolList.txt", "r")
symbols = []
for name in f:
    symbols.append(name[:-1])
today = datetime.datetime.now()
findMissingDates(today,0)
print(path.exists("Incremental -" + formDate(today) + ".csv"))