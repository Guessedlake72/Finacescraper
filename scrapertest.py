import yfinance as yf
import csv
import os

try:
    os.makedirs("Market Scraper/Initial") 
    print("Directory created successfully") 
except OSError as error: 
    print("Directory can not be created" ) 

symbol = "MSFT"
msft = yf.Ticker(symbol)
hist = msft.history(period="max")
hist.to_csv("Market Scraper/Initial/" + symbol + ".txt")