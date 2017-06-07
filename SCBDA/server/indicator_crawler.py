
# coding: utf-8

# In[1]:

########### Import libraries ###########
import requests
#beautifulsoup用於解析html或xml等標籤語言的文檔
import pandas

from bs4 import BeautifulSoup


# In[10]:

def indicatortable_crawler():
    url = 'http://stockq.org'
    html = requests.get(url,headers = headers)
    html.encoding = 'utf8'
    soup = BeautifulSoup(''.join(html.text),"html.parser")
    table_list = soup.findAll('table',{'class':'marketdatatable'})
    return table_list


# In[5]:

import requests
import pandas
from bs4 import BeautifulSoup

def indicator_Asia():
    df = pandas.read_html('http://www.stockq.org/market/asia.php')
    df2 = df[7][1:]
    df2.columns = df2.iloc[0]
    df_Asia = df2.drop(df2.index[0])
    return df_Asia
df_Asia = indicator_Asia()

def indicator_Europe():
    df = pandas.read_html('http://www.stockq.org/market/europe.php')
    df2 = df[7][1:]
    df2.columns = df2.iloc[0]
    df_Europe = df2.drop(df2.index[0])
    return df_Europe
df_Europe = indicator_Europe()

def indicator_America():
    df = pandas.read_html('http://www.stockq.org/market/america.php')
    df2 = df[7][1:]
    df2.columns = df2.iloc[0]
    df_America = df2.drop(df2.index[0])
    return df_America
df_America = indicator_America()


# In[3]:

def indicatorPlot_Asia():
    stockname_list = df_Asia['股市'].tolist()
    indicator_list = df_Asia['指數'].tolist()
    mainlist = []
    for index in range(0,len(stockname_list)):
        tmp_list =[stockname_list[index],indicator_list[index]]
        mainlist.append(tmp_list)
    print(mainlist)


# In[9]:

def indicatorPlot_Europe():
    stockname_list = df_Europe['股市'].tolist()
    indicator_list = df_Europe['指數'].tolist()
    mainlist = []
    for index in range(0, len(stockname_list)):
        tmp_list = [stockname_list[index], indicator_list[index]]
        mainlist.append(tmp_list)
    print(mainlist)


# In[10]:

def indicatorPlot_America():
    stockname_list = df_America['股市'].tolist()
    indicator_list = df_America['指數'].tolist()
    mainlist = []
    for index in range(0, len(stockname_list)):
        tmp_list = [stockname_list[index], indicator_list[index]]
        mainlist.append(tmp_list)
    print(mainlist)


# In[11]:


# In[48]:

import requests
import pandas
from bs4 import BeautifulSoup

def indicator_Europe():
    df = pandas.read_html('http://www.stockq.org/market/europe.php')
    df2 = df[7][1:]
    df2.columns = df2.iloc[0]
    df_Europe = df2.drop(df2.index[0])
    return df_Europe


# In[49]:

import requests
import pandas
from bs4 import BeautifulSoup

def indicator_America():
    df = pandas.read_html('http://www.stockq.org/market/america.php')
    df2 = df[7][1:]
    df2.columns = df2.iloc[0]
    df_America = df2.drop(df2.index[0])
    return df_America

