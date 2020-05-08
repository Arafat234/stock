from django.shortcuts import render
import numpy as np
import pandas as pd
import json
import requests
import math
from .models import searchresults,mystock,news
from django.http import JsonResponse
from sklearn import preprocessing
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn import metrics
from datetime import timedelta,date,datetime
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.
@csrf_exempt
def retrievestockinfo(request):


        closeprices = []
        openprices = []
        highprices = []
        volume = []

        value = []
        value1 = []
        value2 = []
        value3 =[]

        value1samecounter = 0
        value1upcounter = 0
        value1downcounter = 0

        value2samecounter = 0
        value2upcounter = 0
        value2downcounter = 0

        value3samecounter = 0
        value3upcounter = 0
        value3downcounter = 0

        currentClosePrice = 0
        currentOpenPrice = 0
        currentHighPrice = 0
        currentVolume = 0

        totallength = 0





        datastore = []
        dates = []
        startdates = ''
        enddates = ''
        count = 0
        companyname = ''
        description = ''
        countersss = 0

        if request.method == 'POST':

            a = request.POST.get('startDate')
            b = request.POST.get('endDate')

            startdates = datetime.strptime(a, "%Y-%m-%d")
            enddates = datetime.strptime(b, "%Y-%m-%d")


            details = {
                'symbol':'',
                'name': '',
                'currentprice':'',
                'open': '',
                'high': '',
                'low': '',
                'close': '',
                'volume': '',

                'currency': '',
                'changepercentage': '',
                'volumeaverage': '',
                'shares': '',
                'time': '',
                'timezone': '',
                'timezonename': '',

                '52high': '',
                '52low': '',
                'description': '',

                'dates': '',
                'datastore': '',
                'estimate': ''
            }




            stockname = request.POST.get('stockname')
            defaultstockname = stockname

            qs = searchresults.objects.all()

            for i in qs:
                if stockname == i.company_name:
                    companyname = i.company_name
                    stockname = i.symbol
                    description = i.description
                    break
            else:
                stockname = 'LSE.L'
                companyname = 'LSE London Stock Exchange Plc'
                description = "London Stock Exchange is a stock exchange in the City of London, England. As of April 2018, London Stock Exchange had a market capitalisation of US$4.59 trillion. It was founded in 1571, making it one of the oldest exchanges in the world.Its current premises are situated in Paternoster Square close to St Paul's Cathedral in the City of London. It is part of London Stock Exchange Group (LSEG). London Stock Exchange Group was created in October 2007 when London Stock Exchange merged with Milan Stock Exchange, Borsa Italiana."

            try:
                print("Exception Field")
                stockdetail = searchresults.objects.get(company_name = companyname)
                json_data = stockdetail.field

                for eachdate in pd.date_range(startdates, enddates):

                   try:
                      closeprices.append(json_data['history'][eachdate.strftime("%Y-%m-%d")]['close'])
                      openprices.append(json_data['history'][eachdate.strftime("%Y-%m-%d")]['open'])
                      highprices.append(json_data['history'][eachdate.strftime("%Y-%m-%d")]['high'])
                      volume.append(json_data['history'][eachdate.strftime("%Y-%m-%d")]['volume'])
                      dates.append(eachdate.strftime("%Y-%m-%d"))

                   except:
                        pass

                for i in range(len(closeprices)):
                    if i == 0:
                        currentClosePrice = closeprices[i]
                        value.append('same')

                    elif closeprices[i] > currentClosePrice:
                        currentClosePrice = closeprices[i]
                        value.append('increase')

                    elif closeprices[i] == currentClosePrice:
                         currentClosePrice = closeprices[i]
                         value.append('same')
                    else:
                        value.append('decrease')
                        currentClosePrice = closeprices[i]

                for i in range(len(openprices)):
                    if i == 0:
                        currentOpenPrice = openprices[i]
                        value1.append('same')
                        value1samecounter+=1

                    elif openprices[i] > currentOpenPrice:
                        currentOpenPrice = openprices[i]
                        value1.append('up')
                        value1upcounter+=1

                    elif openprices[i] == currentOpenPrice:
                         currentOpenPrice = openprices[i]
                         value1.append('same')
                         value1samecounter+=1

                    else:
                        value1.append('down')
                        currentOpenPrice = openprices[i]
                        value1downcounter+=1

                for i in range(len(highprices)):
                    if i == 0:
                        currentHighPrice = highprices[i]
                        value2.append('same')
                        value2samecounter+=1

                    elif highprices[i] > currentHighPrice:
                         currentHighPrice = highprices[i]
                         value2.append('up')
                         value2upcounter+=1

                    elif highprices[i] == currentHighPrice:
                         currentHighPrice = highprices[i]
                         value2.append('same')
                         value2samecounter+=1

                    else:
                        value2.append('down')
                        currentHighPrice = highprices[i]
                        value2downcounter+=1

                for i in range(len(volume)):
                    if i == 0:
                        currentVolume = volume[i]
                        value3.append('same')
                        value3samecounter+=1

                    elif volume[i] > currentHighPrice:
                         currentVolume = volume[i]
                         value3.append('up')
                         value3upcounter+=1

                    elif highprices[i] == currentHighPrice:
                         currentVolume = volume[i]
                         value3.append('same')
                         value3samecounter+=1

                    else:
                        value3.append('down')
                        currentVolume = volume[i]
                        value3downcounter+=1

                def findmaxlst(a,b,c): # only done on features

                    if a >= b and a >= c:
                        return 1
                    elif b >= a and b >= c:
                        return 2
                    else:
                        return 0

                predictorvalue1 = findmaxlst(value1samecounter,value1upcounter,value1downcounter)
                predictorvalue2 = findmaxlst(value2samecounter,value2upcounter,value2downcounter)
                predictorvalue3 = findmaxlst(value3samecounter,value3upcounter,value3downcounter)


                le = preprocessing.LabelEncoder()
                a = le.fit_transform(value1)
                b = le.fit_transform(value2)
                c = le.fit_transform(value3)

                labelleddata = le.fit_transform(value)

                features=list(zip(a,b,c))

                X_train, X_test, y_train, y_test = train_test_split(features, labelleddata, test_size=0.3,random_state=109)

                gnb = MultinomialNB(alpha = 1.0)
                gnb.fit(X_train, y_train)
                y_pred = gnb.predict(X_test)


                var = str(gnb.predict([[predictorvalue1,predictorvalue2,predictorvalue3]]))
                probabilties = gnb.predict_proba([[predictorvalue1,predictorvalue2,predictorvalue3]])
                print(var)
                print(probabilties)




                def results(var):
                    if var == '[1]' and probabilties[0][1] != 0:
                        v = stockname + ' stock close price is likely to go up with a probability of ' + str(int(probabilties[0][1] * 100)) + '%'
                        return v
                    elif var =='[2]' and probabilties[0][2] != 0:
                        v = stockname + ' stock close price is likely to stay the same with a probability of ' + str(int(probabilties[0][2] * 100)) + '%'
                        return v
                    else:
                        v = stockname +  ' stock close price is likely to go down with a probability of ' + str(int(probabilties[0][0] * 100)) + '%'
                        return v



                calculations = results(var)
                print(calculations)


                stock = '{}'.format(stockname)

                for i in range(len(closeprices)):
                    datastore.append(closeprices[i])

                print("Exception field1")
                stockdetails = searchresults.objects.get(company_name = companyname)
                json_datas = stockdetails.field1

                details = {
                    'symbol':json_datas['data'][0]['symbol'],
                    'name': json_datas['data'][0]['name'],
                    'currentprice':json_datas['data'][0]['price'],
                    'open': json_datas['data'][0]['price_open'],
                    'high': json_datas['data'][0]['day_high'],
                    'low': json_datas['data'][0]['day_low'],
                    'close': json_datas['data'][0]['close_yesterday'],
                    'volume': json_datas['data'][0]['volume'],

                    'currency': json_datas['data'][0]['currency'],
                    'changepercentage': json_datas['data'][0]['change_pct'],
                    'volumeaverage': json_datas['data'][0]['volume_avg'],
                    'shares': json_datas['data'][0]['shares'],
                    'time': json_datas['data'][0]['last_trade_time'],
                    'timezone': json_datas['data'][0]['timezone'],
                    'timezonename': json_datas['data'][0]['timezone_name'],

                    '52high': json_datas['data'][0]['52_week_high'],
                    '52low': json_datas['data'][0]['52_week_low'],
                    'description': description,

                    'dates': dates,
                    'datastore': datastore,
                    'estimate': calculations
                    }

            except:
                pass
            return JsonResponse(details)
        else:
            return render (request,'stock/stockinformation.html',{})

@csrf_exempt
@login_required
def addstockinfo(request):
    if request.method == 'POST':
        a = request.POST.get('stockname')
        if mystock.objects.filter(stockname = a,username = request.user).exists():
            context = {'value':'none'}
            return JsonResponse(context)
        else:
            b = mystock.objects.create(stockname = a)
            b.username = request.user
            b.save()
            context = {'value':'hello'}
            return JsonResponse(context)

@csrf_exempt
@login_required
def mystockinfo(request):

    qs = mystock.objects.all()
    for i in qs:
        addmystockinfoss(request,i.stockname)
    queryset = mystock.objects.filter(username = request.user)
    context = {
        'object_list' : queryset
    }
    return render (request,'stock/mystock.html',context)

@csrf_exempt
def addmystockinfoss(request,stockname):
    a = stockname
    stockdet = searchresults.objects.get(symbol = stockname)
    json_datas1 = stockdet.field1
    if mystock.objects.filter(stockname = a,username = request.user).exists():
        mystock.objects.filter(stockname = a,username = request.user).update(volume = json_datas1['data'][0]['volume'])
        mystock.objects.filter(stockname = a,username = request.user).update(open = json_datas1['data'][0]['price_open'])
        mystock.objects.filter(stockname = a,username = request.user).update(high = json_datas1['data'][0]['day_high'])
        mystock.objects.filter(stockname = a,username = request.user).update(low = json_datas1['data'][0]['day_low'])
        mystock.objects.filter(stockname = a,username = request.user).update(close = json_datas1['data'][0]['close_yesterday'])
        mystock.objects.filter(stockname = a,username = request.user).update(changepct = json_datas1['data'][0]['change_pct'])
        mystock.objects.filter(stockname = a,username = request.user).update(name = json_datas1['data'][0]['name'])
    return

@csrf_exempt
@login_required
def deletemystockinfo(request):
    if request.method == 'POST':
        a = request.POST.get('stockname')
        print(a)
        mystock.objects.filter(name = a,username = request.user).delete()
        return JsonResponse({'hello':'True'})
    return render (request,'stock/mystock.html',{})

@csrf_exempt
def newsinfo(request):
    if request.method == 'GET':
        #r = requests.get('https://stocknewsapi.com/api/v1/category?section=general&items=50&token=qyfpnsvl7pmqfyrr94nsgqrtvmo9eleovbd80rzs').json()
        #news.objects.filter(name = 'one').update(newsfield = r)
        newsdetails = news.objects.get(name = 'one')
        news_json_data = newsdetails.newsfield
        return JsonResponse(news_json_data)
    return render (request,'stock/stockinformation.html',{})
