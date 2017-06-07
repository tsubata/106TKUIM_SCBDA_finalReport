from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

#IndicatorHistory crawler & processing function
import stockQ as sQ
import goodInfo as gI

#test
def index(request):
    return render(request,'index.html')

def getIndicatorHistory(request):
    data = {}
    data['data'] = sQ.getIndicatorHistory()
    data['status'] ="success"
    response = JsonResponse(data)
    response['Access-Control-Allow-Origin'] = '*'
    return response

def getNews(request):
    data = {}
    data['data'] = gI.getNews()
    data['status'] ="success"
    response = JsonResponse(data)
    response['Access-Control-Allow-Origin'] = '*'
    return response

def getStcokPriceTop10(request):
    data = {}
    data['data'] = gI.getStcokPriceTop10()
    data['status'] ="success"
    response = JsonResponse(data)
    response['Access-Control-Allow-Origin'] = '*'
    return response

def getStcokTransactionTop10(request):
    data = {}
    data['data'] = gI.getStcokTransactionTop10()
    data['status'] ="success"
    response = JsonResponse(data)
    response['Access-Control-Allow-Origin'] = '*'
    return response

def getDailyStock(request):
    question = request.GET.get('question', None)
    answer="success"
    response = HttpResponse(answer)
    response['Access-Control-Allow-Origin'] = '*'
    return response

def jquery(request):
    return render(request,'js/jquery-3.2.0.min.js')

def css(request):
    return render(request,'css/style.css')