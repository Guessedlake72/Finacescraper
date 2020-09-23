import yfinance as yf
import csv
import os
import requests



#https://old.nasdaq.com/screening/companies-by-name.aspx?letter=0&exchange=nasdaq&render=download
try:
    os.makedirs("Market Scraper/Initial") 
    print("Directory created successfully") 
except OSError as error: 
    print("Directory can not be created" )
    
try:
    url = 'https://old.nasdaq.com/screening/companies-by-name.aspx?letter=0&exchange=nasdaq&render=download'
    r = requests.get(url, allow_redirects=True)
    open('facebook.ico', 'wb').write(r.content)
except OSError as error: 
    print("File cannot be downloaded" ) 

symbol = "MSFT"
msft = yf.Ticker(symbol)
hist = msft.history(period="max")
hist.to_csv("Market Scraper/Initial/" + symbol + ".txt")