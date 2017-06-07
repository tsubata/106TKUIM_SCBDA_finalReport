
# coding: utf-8

# In[32]:

from bs4 import BeautifulSoup
import pandas as pd
import requests

def Report_TW2317():
    session = requests.Session()
    headers = {"User-Agent":"Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Mobile Safari/537.36",
                "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"}
    url = 'http://goodinfo.tw/StockInfo/StockFinDetail.asp?RPT_CAT=XX_QUAR_ACC&STOCK_ID=2317'
    req = session.get(url, headers = headers)
    req.encoding = 'utf8'
    bsObj = BeautifulSoup(req.text)
    df = pd.read_html(req.text)
    df2 = df[11]
    df2.columns = df2.iloc[0]
    df_TW2317 = df2.drop(df2.index[0])
    df_TW2317 = df_TW2317.drop("2014Q4", axis = 1)
    return(df_TW2317)
#Report_TW2317()



# In[31]:

def Report_TW2330():
    session = requests.Session()
    headers = {"User-Agent":"Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Mobile Safari/537.36",
                "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"}
    url = 'http://goodinfo.tw/StockInfo/StockFinDetail.asp?RPT_CAT=XX_QUAR_ACC&STOCK_ID=2330'
    req = session.get(url, headers = headers)
    req.encoding = 'utf8'
    bsObj = BeautifulSoup(req.text)
    df = pd.read_html(req.text)
    df2 = df[11]
    df2.columns = df2.iloc[0]
    df_TW2330 = df2.drop(df2.index[0])
    df_TW2330 = df_TW2330.drop("2014Q4", axis = 1)
    return(df_TW2330)

#Report_TW2330()

