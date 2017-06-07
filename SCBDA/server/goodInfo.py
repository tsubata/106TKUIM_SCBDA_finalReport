
########### Import libraries ###########
import requests
#beautifulsoup用於解析html或xml等標籤語言的文檔
import pandas

from bs4 import BeautifulSoup


# In[5]:

#爬出股市資料網的table info : list
def indicatortable_crawler():
    url = 'http://goodinfo.tw/StockInfo/index.asp'
    headers = {"User-Agent":"Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Mobile Safari/537.36",
                "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"}
    html = requests.get(url,headers = headers)
    html.encoding = 'utf8'
    soup = BeautifulSoup(''.join(html.text),"html.parser")
    table_list = soup.findAll('table',{'class':'none_tbl'})
    return table_list


# In[19]:

def getNews():
    news_list = []
    table_list = indicatortable_crawler()
    #取出
    for news in table_list[4].findAll("tr"):
        try:
            newsInfo = {}
            #get news classification & title(with link)
            newsInfo['newsclass'] = news.find("nobr").text.replace('\xa0',' ')
            newsInfo['newstitle'] = news.findAll("a")[1].text
            newsInfo['newslink'] = news.findAll("a")[1]["href"][18:].replace("%3A",":").replace("%2F","/").replace("%2E",".").replace("%3F","?").replace("%3D","=")
            newsInfo['newsdate'] = news.find("span").text.replace('\xa0',' ')
            news_list.append(newsInfo)
            #print(newsInfo)
        except:
            print('exception occur')
    return news_list[:10]


# In[68]:

def getStcokPriceTop10():
    main_list = []
    table_list = indicatortable_crawler()
    #取出
    for company in table_list[13].findAll("tr")[:10]:
        list_companyInfo = []
        companyInfo = company.findAll("nobr")
        for index in range(0,len(companyInfo)):
            if index>1:
                list_companyInfo.append(companyInfo[index].text[1:])
            else:
                list_companyInfo.append(companyInfo[index].text)
        main_list.append(list_companyInfo)
        #print("company : "+str(list_companyInfo))
    return main_list[:10]


# In[67]:

def getStcokTransactionTop10():
    main_list = []
    table_list = indicatortable_crawler()
    #取出
    for company in table_list[15].findAll("tr")[:10]:
        list_companyInfo = []
        companyInfo = company.findAll("nobr")
        for index in range(0,len(companyInfo)):
            if index>1:
                list_companyInfo.append(companyInfo[index].text[1:])
            else:
                list_companyInfo.append(companyInfo[index].text)
        main_list.append(list_companyInfo)
        #print("company : "+str(list_companyInfo))
    return main_list[:10]


# In[ ]:



