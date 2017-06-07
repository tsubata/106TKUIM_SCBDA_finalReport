
# coding: utf-8

# In[88]:

import pandas as pd

df = pd.read_html('http://www.stockq.org/index/TWSE.php')
df[15]


# In[80]:

def DowJones():
    df = pd.read_html('http://www.stockq.org/index/INDU.php')
    df2 = df[15]
    df2.columns = ['日期','指數','漲跌比例','1','2','3']
    df_back = df2.drop(['1','2','3'],1)
    df_front = df2.drop(['日期','指數','漲跌比例'],1)
    df_front.columns = ['日期','指數','漲跌比例']
#df_DowJones = df2.drop(df2.index[0])
    df_3 = df_back.append(df_front, ignore_index=True)
    df_DowJones = df_3.drop([0,11])
    return df_DowJones
df_DJ = DowJones()


# In[86]:

def NASDAQ():
    df = pd.read_html('http://www.stockq.org/index/CCMP.php')
    df2 = df[15]
    df2.columns = ['日期','指數','漲跌比例','1','2','3']
    df_back = df2.drop(['1','2','3'],1)
    df_front = df2.drop(['日期','指數','漲跌比例'],1)
    df_front.columns = ['日期','指數','漲跌比例']
    df_3 = df_back.append(df_front, ignore_index=True)
    df_NASDAQ = df_3.drop([0,11])
    return df_NASDAQ
df_NASDAQ = NASDAQ()


# In[89]:

def TWSE():
    df = pd.read_html('http://www.stockq.org/index/TWSE.php')
    df2 = df[15]
    df2.columns = ['日期','指數','漲跌比例','1','2','3']
    df_back = df2.drop(['1','2','3'],1)
    df_front = df2.drop(['日期','指數','漲跌比例'],1)
    df_front.columns = ['日期','指數','漲跌比例']
    df_3 = df_back.append(df_front, ignore_index=True)
    df_TWSE = df_3.drop([0,11])
    return df_TWSE
df_TWSE = TWSE()


# In[92]:

def getIndicatorHistory():
    date_list = df_DJ['日期'].tolist()
    DJ_list = df_DJ['指數'].tolist()
    NASDAQ_list = df_NASDAQ['指數'].tolist()
    TWSE_list = df_TWSE['指數'].tolist()
    mainlist = []
    for index in range(0, len(date_list)):
        tmp_list = [1+index, round(float(DJ_list[index])/21,1), round(float(NASDAQ_list[index])/6,1), round(float(TWSE_list[index])/10,1)]
        mainlist.append(tmp_list)
    return mainlist

