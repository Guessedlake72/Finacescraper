import yfinance as yf
import os
import datetime


#https://old.nasdaq.com/screening/companies-by-name.aspx?letter=0&exchange=nasdaq&render=download

today = datetime.datetime.now()
def formDate(date):
    return date.strftime("%Y") + "-" + date.strftime("%m") + "-" + date.strftime("%d")

try:
    os.makedirs("Initial -" + formDate(today)) 
    print("Directory created successfully") 
except OSError as error: 
    print("Directory can not be created" )

f = open("symbolfetcher/symbolList.txt", "r")
symbols = []
for name in f:
    symbols.append(name[:-1])

for symbol in symbols:
    tick = yf.Ticker(symbol)
    hist = tick.history(period="max")
    hist.to_csv("Initial -" + formDate(today) +"/" + symbol + ".csv")