# coding: utf-8
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'), #open index.html
    url(r'^js/jquery-3.2.0.min.js/$', views.jquery, name='jquery'), #load jquery
    url(r'^css/style.css/$', views.css, name='css'), #load css
    #api
    url(r'^api/getDailyStock/$', views.getDailyStock, name='getDailyStock'),
    url(r'^api/getNews/$', views.getNews, name='getNews'),
    url(r'^api/getStcokPriceTop10/$', views.getStcokPriceTop10, name='getStcokPriceTop10'),
    url(r'^api/getIndicatorHistory/$', views.getIndicatorHistory, name='getIndicatorHistory'),
    url(r'^api/getStcokTransactionTop10/$', views.getStcokTransactionTop10, name='getStcokTransactionTop10'),

]