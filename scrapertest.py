import yfinance as yf
import csv
import os

try:
    os.makedirs("Market Scraper/Example") 
    print("Directory created successfully") 
except OSError as error: 
    print("Directory can not be created" ) 

file1 = open("Market Scraper/Example/hello.txt", "a")
toFile = "lololol"
file1.write(toFile)
file1.close()


msft = yf.Ticker("MSFT")
msft.info
#hist = msft.history(period="max")
#hist.to_csv('file_name.csv')