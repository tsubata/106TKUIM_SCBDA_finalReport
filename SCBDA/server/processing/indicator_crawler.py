# coding: utf-8
import requests
import pandas
from bs4 import BeautifulSoup

def indicatortable_crawler():
    url = 'http://stockq.org'
    html = requests.get(url)
    html.encoding = 'utf8'
    soup = BeautifulSoup(''.join(html.text),"html.parser")
    table_list = soup.findAll('table',{'class':'marketdatatable'})
    return table_list

def indicator_Asia():
    df = pandas.read_html('http://www.stockq.org/market/asia.php')
    df2 = df[7][1:]
    df2.columns = df2.iloc[0]
    df_Asia = df2.drop(df2.index[0])
    return df_Asia


def indicator_Europe():
    df = pandas.read_html('http://www.stockq.org/market/europe.php')
    df2 = df[7][1:]
    df2.columns = df2.iloc[0]
    df_Europe = df2.drop(df2.index[0])
    return df_Europe

def indicator_America():
    df = pandas.read_html('http://www.stockq.org/market/america.php')
    df2 = df[7][1:]
    df2.columns = df2.iloc[0]
    df_America = df2.drop(df2.index[0])
    return df_America


