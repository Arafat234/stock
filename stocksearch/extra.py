# try:
#         stock = '{}'.format(stockname)
#         r = requests.get('https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={}&apikey=7MY5J6080Y5P50DW.'.format(stock)).json()
#         #r = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={}&apikey=7MY5J6080Y5P50DW.'.format(stock)).json()
#         #r = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={}&interval=5min&apikey=7MY5J6080Y5P50DW.'.format(stock)).json()
#         #todays = '{}'.format(date.today())
#         #todays = '2020-01-24'.format(date.today())
#         #todays = datetime.today().strftime('%Y-%m-%d')
#         #print(todays)
#         details = {
#             'symbol':stock.upper(),
#             'open':r['Global Quote']['02. open'],
#             'high':r['Global Quote']['03. high'],
#             'low':r['Global Quote']['04. low'],
#             'close':r['Global Quote']['05. price'],
#             'volume':r['Global Quote']['06. volume'],
#
#         }
#         # todays = '2020-01-30'
#         # details = {
#         #     'symbol':stock.upper(),
#         #     'open':r['Time Series (Daily)'][todays]['1. open'],
#         #     'high':r['Time Series (Daily)'][todays]['2. high'],
#         #     'low':r['Time Series (Daily)'][todays]['3. low'],
#         #     'close':r['Time Series (Daily)'][todays]['4. close'],
#         #     'volume':r['Time Series (Daily)'][todays]['5. volume'],
#         #
#         # }
#         #template_name = 'stocksearch/stockinformation.html'
#         template_name = 'stocksearch/stockinformation.html'
#         return render (request,template_name,details)
# # return render (request,template_name)
# except:
#         details = {
#             'symbol':'',
#             'open':'',
#             'high':'',
#             'low':'',
#             'close':'',
#             'volume':'',
#             'error':'error'
#         }
#         return render (request,template_name,details)
















# def retrievestockinfoo(request):
    # datastore = []
    # if request.method == 'POST':
    #     details = {
    #         'symbol':'',
    #         'name': '',
    #         'currentprice':'',
    #         'open':'',
    #         'high': '',
    #         'low': '',
    #         'close': '',
    #         'volume': '',
    #     }
    #
    #     stockname = request.POST.get('stockname')
    #     startm = request.POST.get('startDate')
    #     endm = request.POST.get('endDate')
    #
    #
    #     qs = searchresults.objects.all()
    #
    #     for i in qs:
    #         if stockname == i.company_name:
    #             stockname = i.symbol
    #             break
    #     try:
    #
    #         # df = web.DataReader(stockname, data_source='yahoo',start = 2020-02-01,end = 2020-02-12)
    #         # ab = df.to_json(orient='records')
    #         # the_dict = json.loads(ab)
    #         # stock = '{}'.format(stockname)
    #         # r = requests.get('https://api.worldtradingdata.com/api/v1/stock?symbol={}&api_token=tsNxMjm41n3RocYkyWfIgB6xk1Z1RRahzAjzJk3pY6yQv8LR8h90kBonygk5'.format(stock)).json()
    #         # details = {
    #         #     'symbol':r['data'][0]['symbol'],
    #         #     'name': r['data'][0]['name'],
    #         #     'currentprice':r['data'][0]['price'],
    #         #     'open': r['data'][0]['price_open'],
    #         #     'high': r['data'][0]['day_high'],
    #         #     'low': r['data'][0]['day_low'],
    #         #     'close': r['data'][0]['close_yesterday'],
    #         #     'volume': r['data'][0]['volume'],
    #         # }
    #     except:
    #         pass
    #     return JsonResponse(details)
    # else:
    #     return render (request,'stocksearch/stockinformation.html',{})

    # stockname = request.GET.get('stockname')
    #
    #
    # qs = searchresults.objects.all()
    #
    # for i in qs:
    #     if stockname == i.company_name:
    #         stockname = i.symbol
    #         break
    #
    #
    #
    #
    #stockname = request.GET.get('stockname')

    # template_name = 'stocksearch/stockinformation.html'
    # #
    # #
    # try:
    #
    #     df = web.DataReader('AAPL', data_source='yahoo', start='2020-02-03', end='2020-02-03')
    #     ab = df.to_json(orient='records')
    #     the_dict = json.loads(ab)




        # details = {
        #             'symbol':stockname.upper(),
        #             'open':str(the_dict[0]['Open']),
        #             'high':str(the_dict[0]['High']),
        #             'low':str(the_dict[0]['Low']),
        #             'close':str(the_dict[0]['Close']),
        #             'volume':str(the_dict[0]['Volume']),
        #             'error':'error'
        #         }


        # stock = '{}'.format(stockname)
        # r = requests.get('https://api.worldtradingdata.com/api/v1/stock?symbol={}&api_token=tsNxMjm41n3RocYkyWfIgB6xk1Z1RRahzAjzJk3pY6yQv8LR8h90kBonygk5'.format(stock)).json()
        # details = {
        #     'symbol':r['data'][0]['symbol'],
        #     'name': r['data'][0]['name'],
        #     'currentprice':r['data'][0]['price'],
        #     'open': r['data'][0]['price_open'],
        #     'high': r['data'][0]['day_high'],
        #     'low': r['data'][0]['day_low'],
        #     'close': r['data'][0]['close_yesterday'],
        #     'volume': r['data'][0]['volume'],
        # }
        # return render (request,template_name,details)

    # except:
    #         details = {
    #             'symbol':'',
    #             'name': '',
    #             'currentprice':'',
    #             'open':'',
    #             'high': '',
    #             'low': '',
    #             'close': '',
    #             'volume': '',
    #         }
    #         return render (request,template_name,details)





            #
            # // function getDates(startDate, stopDate){
            # //
            # //         var currentDate = moment(startDate);
            # //         var stopDate = moment(stopDate);
            # //         while (currentDate <= stopDate) {
            # //
            # //             currentDate = moment(currentDate).add(1, 'days');
            # //             count = count + 1
            # //         }
            # //         return count;
            # // };





















    # Create your views here.

    #def retrievestockinfo(request):
        # stockname = request.GET.get('stockname')
        # qs = searchresults.objects.all()
        # template_name = 'stocksearch/stockinformation.html'
        # for i in qs:
        #     if stockname == i.company_name:
        #             stockname = i.symbol
        #             break
        # try:
        #         stock = '{}'.format(stockname)
        #         r = requests.get('https://api.worldtradingdata.com/api/v1/stock?symbol={}&api_token=tsNxMjm41n3RocYkyWfIgB6xk1Z1RRahzAjzJk3pY6yQv8LR8h90kBonygk5'.format(stock)).json()
        #         details = {
        #             'symbol':r['data'][0]['symbol'],
        #             'name': r['data'][0]['name'],
        #             'currentprice':r['data'][0]['price'],
        #             'open': r['data'][0]['price_open'],
        #             'high': r['data'][0]['day_high'],
        #             'low': r['data'][0]['day_low'],
        #             'close': r['data'][0]['close_yesterday'],
        #             'volume': r['data'][0]['volume'],
        #         }
        #         return render(request,template_name,details)
        # except:
        #         details = {
        #                 'symbol':'',
        #                 'name': '',
        #                 'currentprice':'',
        #                 'open':'',
        #                 'high': '',
        #                 'low': '',
        #                 'close': '',
        #                 'volume': '',
        #         }
        #         return render(request,template_name,details)


    # def retrievestockinfo(request):
    #     # Machine learning variables
    #     value = []
    #     value1 = []
    #     value2 = []
    #     value1samecounter = 0
    #     value1upcounter = 0
    #     value1downcounter = 0
    #     value2samecounter = 0
    #     value2upcounter = 0
    #     value2downcounter = 0
    #     currentClosePrice = 0
    #     currentOpenPrice = 0
    #     currentHighPrice = 0
    #     # Machine learning variables
    #
    #     datastore = []
    #     startdates = '2020-01-01'
    #     enddates = datetime.today().strftime('%Y-%m-%d')
    #
    #
    #
    #     if request.method == 'POST':
    #         details = {
    #             'symbol':'',
    #             'name': '',
    #             'currentprice':'',
    #             'open': '',
    #             'high': '',
    #             'low': '',
    #             'close': '',
    #             'volume': '',
    #             'start': '',
    #             'end': '',
    #             'datastore': '',
    #             'estimate':''
    #         }
    #
    #         stockname = request.POST.get('stockname')
    #         qs = searchresults.objects.all()
    #         for i in qs:
    #             if stockname == i.company_name:
    #                 stockname = i.symbol
    #                 break
    #         try:
    #             df = web.DataReader(stockname, data_source='yahoo',start = startdates ,end = enddates)
    #             ab = df.to_json(orient='records')
    #             the_dict = json.loads(ab)
    #
    #             # Machine learning
    #             for i in range(len(the_dict)):
    #                 if i == 0:
    #                     currentClosePrice = the_dict[i]['Close']
    #                     value.append('same')
    #                 elif the_dict[i]['Close'] > currentClosePrice:
    #                     currentClosePrice = the_dict[i]['Close']
    #                     value.append('increase')
    #                 elif the_dict[i]['Close'] == currentClosePrice:
    #                      currentClosePrice = the_dict[i]['Close']
    #                      value.append('same')
    #                 else:
    #                     value.append('decrease')
    #                     currentClosePrice = the_dict[i]['Close']
    #
    #
    #             for i in range(len(the_dict)):
    #                 if i == 0:
    #                     currentOpenPrice = the_dict[i]['Open']
    #                     value1.append('same')
    #                     value1samecounter+=1
    #                 elif the_dict[i]['Open'] > currentOpenPrice:
    #                     currentOpenPrice = the_dict[i]['Open']
    #                     value1.append('up')
    #                     value1upcounter+=1
    #                 elif the_dict[i]['Open'] == currentOpenPrice:
    #                      currentOpenPrice = the_dict[i]['Open']
    #                      value1.append('same')
    #                      value1samecounter+=1
    #                 else:
    #                     value1.append('down')
    #                     currentOpenPrice = the_dict[i]['Open']
    #                     value1downcounter+=1
    #
    #
    #             for i in range(len(the_dict)):
    #                 if i == 0:
    #                     currentHighPrice = the_dict[i]['High']
    #                     value2.append('same')
    #                     value2samecounter+=1
    #                 elif the_dict[i]['High'] > currentHighPrice:
    #                     currentHighPrice = the_dict[i]['High']
    #                     value2.append('up')
    #                     value2upcounter+=1
    #                 elif the_dict[i]['High'] == currentHighPrice:
    #                      currentHighPrice = the_dict[i]['High']
    #                      value2.append('same')
    #                      value2samecounter+=1
    #                 else:
    #                     value2.append('down')
    #                     currentHighPrice = the_dict[i]['High']
    #                     value2downcounter+=1
    #
    #             def findmaxlst1():
    #                 if value1samecounter >= value1upcounter and value1samecounter >= value1downcounter:
    #                     return 1
    #                 elif value1upcounter >= value1samecounter and value1upcounter >= value1downcounter:
    #                     return 2
    #                 else:
    #                     return 0
    #
    #
    #             def findmaxlst2():
    #                 if value2samecounter >= value2upcounter and value2samecounter >= value2downcounter:
    #                     return 1
    #                 elif value2upcounter >= value2samecounter and value2upcounter >= value2downcounter:
    #                     return 2
    #                 else:
    #                     return 0
    #
    #             predictorvalue1 = findmaxlst1()
    #             predictorvalue2 = findmaxlst2()
    #
    #             le = preprocessing.LabelEncoder()
    #             a = le.fit_transform(value1)
    #             b = le.fit_transform(value2)
    #             labelleddata = le.fit_transform(value)
    #
    #             features=list(zip(a,b))
    #
    #             X_train, X_test, y_train, y_test = train_test_split(features, labelleddata, test_size=0.3,random_state=109)
    #             gnb = GaussianNB()
    #             gnb.fit(X_train, y_train)
    #             y_pred = gnb.predict(X_test)
    #
    #             var = str(gnb.predict([[predictorvalue1,predictorvalue2]]))
    #             probabilties = gnb.predict_proba([[predictorvalue1,predictorvalue2]])
    #
    #             def results(var):
    #                 if var == '[1]':
    #                     a = 'stock close price is likely to increase with a probability of'
    #                     b = str(probabilties[0][1])
    #                     c = a + b
    #                     return c
    #                     #print(stockname + ' stock close price is likely to increase with a probability of ' + str(probabilties[0][1]))
    #                 elif var =='[2]':
    #                     a = ' stock close price is likely to stay the same with a probability of '
    #                     b = str(probabilties[0][2])
    #                     c = a + b
    #                     return c
    #                     #print(stockname + ' stock close price is likely to stay the same with a probability of ' + str(probabilties[0][2]))
    #                 else:
    #                     a = ' stock close price is likely to stay the same with a probability of '
    #                     b = str(probabilties[0][0])
    #                     c = a + " " + b
    #                     return c
    #                     #print(stockname +  ' stock close price is likely to go down with a probability of ' + str(probabilties[0][0]))
    #
    #
    #             calculations = results(var)
    #             print(calculations)
    #             # Machine learning
    #
    #             stock = '{}'.format(stockname)
    #
    #             for i in range(len(the_dict)):
    #                 datastore.append(the_dict[i]['Close'])
    #
    #
    #
    #             r = requests.get('https://api.worldtradingdata.com/api/v1/stock?symbol={}&api_token=tsNxMjm41n3RocYkyWfIgB6xk1Z1RRahzAjzJk3pY6yQv8LR8h90kBonygk5'.format(stock)).json()
    #
    #
    #
    #
    #             details = {
    #                 'symbol':r['data'][0]['symbol'],
    #                 'name': r['data'][0]['name'],
    #                 'currentprice':r['data'][0]['price'],
    #                 'open': r['data'][0]['price_open'],
    #                 'high': r['data'][0]['day_high'],
    #                 'low': r['data'][0]['day_low'],
    #                 'close': r['data'][0]['close_yesterday'],
    #                 'volume': r['data'][0]['volume'],
    #                 'start': startdates,
    #                 'end': enddates,
    #                 'datastore': datastore,
    #                 'estimate': calculations
    #                 }
    #
    #
    #
    #
    #
    #
    #
    #         except:
    #             pass
    #         return JsonResponse(details)
    #     else:
    #         return render (request,'stocksearch/stockinformation.html',{})




    # <!-- <div class="input-group mb-3 d-flex justify-content-center">
    #       <input type="text" class="form-control" value="" id ="search" placeholder="Enter FTSE 100 Stock" aria-label="FTSE 100" aria-describedby="basic-addon2">
    #       <div class="input-group-append">
    #         <button class="btn btn-outline-secondary" onclick="search();" type="button">Search</button>
    #       </div>
    # </div> -->





    # // function page() {
    # //     $.ajax({
    # //        url: "{% url 'stockinfo' %}",
    # //        method: 'POST',
    # //        data:{
    # //          stockname: 'LSE.L',
    # //          startDate : startdate,
    # //          endDate : enddate,
    # //          csrfmiddlewaretoken: '{{ csrf_token }}',
    # //        },
    # //        success: function(data) {
    # //           // console.log(document.getElementById('search').value.substring(4,))
    # //           console.log("mark")
    # //           //currentstockname  = document.getElementById('search').value
    # //           loadsearchinformation(data)
    # //           getnews(data['symbol'])
    # //           document.getElementById('search').value = ''
    # //        }
    # //     })
    # // };




    # // function getDates(startDate, stopDate) {
    # //         var dateArray = [];
    # //         var currentDate = moment(startDate);
    # //         var stopDate = moment(stopDate);
    # //         while (currentDate <= stopDate) {
    # //             dateArray.push( moment(currentDate).format('YYYY-MM-DD') )
    # //             currentDate = moment(currentDate).add(1, 'days');
    # //         }
    # //         return dateArray;
    # //     };
    # // function formatDate(date) {
    # //         var d = new Date(date),
    # //             month = '' + (d.getMonth() + 1),
    # //             day = '' + d.getDate(),
    # //             year = d.getFullYear();
    # //
    # //         if (month.length < 2)
    # //             month = '0' + month;
    # //         if (day.length < 2)
    # //             day = '0' + day;
    # //
    # //         return [year, month, day].join('-');
    # //     };





    # function loadbookmarkstock(a){
    #
    #        if(a)
    #        {
    #            $.ajax({
    #               url :"https://api.worldtradingdata.com/api/v1/stock?symbol=" + a + "&api_token=tsNxMjm41n3RocYkyWfIgB6xk1Z1RRahzAjzJk3pY6yQv8LR8h90kBonygk5",
    #               method: 'GET',
    #               data:{
    #                 // fallback : true,
    #                 csrfmiddlewaretoken: '{{ csrf_token }}',
    #               },
    #               success: function(data) {
    #                  console.log(data['data'][0]['symbol'])
    #                   output = output + '<div>'
    #                   + '<div>' + data['data'][0]['symbol'] + '</div>'
    #                   + '<div>' + data['data'][0]['name'] + '</div>'
    #                   + '</div>'
    #
    #                   document.getElementById('mystock').innerHTML = output;
    #
    #               //    try{
    #               //    for (i = 0; i < 100; i++) {
    #               //        starter = moment().subtract(i, "days").format('YYYY-MM-DD');
    #               //        try{
    #               //        console.log(data['history'][starter]['open'])
    #               //        output = output + '<div>' + data['history'][starter]['open'] + '</div>'
    #               //        break
    #               //           }
    #               //       catch{
    #               //       }
    #               //    }
    #               //   }
    #               //   catch{
    #               //        document.getElementById('mystock').innerHTML = output;
    #               //   }
    #               //    document.getElementById('mystock').innerHTML = output;
    #               // }
    #
    #
    #
    #           }
    #       })
    #     }
    # };

        # // function getnews(){
        # //     // redo this function
        # //        // if(name)
        # //        // {
        # //            $.ajax({
        # //               //url: "https://stocknewsapi.com/api/v1?tickers=" + name + "&items=50&token=qyfpnsvl7pmqfyrr94nsgqrtvmo9eleovbd80rzs",
        # //               url: "https://stocknewsapi.com/api/v1/category?section=general&items=50&token=qyfpnsvl7pmqfyrr94nsgqrtvmo9eleovbd80rzs",
        # //               method: 'GET',
        # //               data:{
        # //                 // fallback : true,
        # //                 csrfmiddlewaretoken: '{{ csrf_token }}',
        # //               },
        # //               success: function(data) {
        # //                  //  var output;
        # //                  //  for (var i in data["data"]){
        # //                  //     output += '<h4>${data["data"][i]["news_url"]}</h4>';
        # //                  // "<img src="data["data"][i]["image_url"]" alt="News">"
        # //                  // }
        # //                  //'<div class="card-header">' + "<p>'image'</p>" + '</img>'  + '</div>'
        # //                  //"<div>" +  '<div class="card-header">' +  + '</div>'
        # //                  for (var i in data["data"]){
        # //
        # //                  output = output +   '<div class="card-image">' +  "<img src=" + '"' + data["data"][i]["image_url"] + '"' + "/>" +  '</div>' +'<div class="card-body">' + "<a href=" + data["data"][i]["news_url"] + ">" + "</a>" + '</div>'
        # //                  if (i == 5){
        # //                    break
        # //                     }
        # //
        # //                 }
        # //               document.getElementById('news').innerHTML = output;
        # //               output = ''
        # //               }
        # //            });
        # //
        # //        // }
        # //
        # //    };

        # // var options = {
        # //                data: [
        # //                            "AAL Anglo American",
        # //                            "ABF Associated British Foods",
        # //                            "ADM Admiral",
        # //                            "AHT Ashtead",
        # //                            "ANTO Antofagasta",
        # //                            "AUTO Auto Trader",
        # //                            "AV. Aviva",
        # //                            "AVV Aveva",
        # //                            "AZN Astrazeneca",
        # //                            "BA. BAE Systems",
        # //                            "BARC Barclays",
        # //                            "BATS BAT",
        # //                            "BDEV Barratt Developments",
        # //                            ]
        # //                 };
        # // var startdate = String(moment().subtract(29, 'days').format('YYYY-MM-DD'))
        # // var enddate = String(moment().format('YYYY-MM-DD'))

    # @csrf_exempt
    # @login_required
    # def addmystockinfo(request):
    #     if request.method == 'POST':
    #         a = request.POST.get('stockname')
    #         r = requests.get('https://api.worldtradingdata.com/api/v1/stock?symbol={}&api_token=tsNxMjm41n3RocYkyWfIgB6xk1Z1RRahzAjzJk3pY6yQv8LR8h90kBonygk5'.format(a)).json()
    #         if mystock.objects.filter(stockname = a,username = request.user).exists():
    #             mystock.objects.filter(stockname = a,username = request.user).update(volume = r['data'][0]['volume'])
    #             mystock.objects.filter(stockname = a,username = request.user).update(open = r['data'][0]['price_open'])
    #             mystock.objects.filter(stockname = a,username = request.user).update(high = r['data'][0]['day_high'])
    #             mystock.objects.filter(stockname = a,username = request.user).update(low = r['data'][0]['day_low'])
    #             mystock.objects.filter(stockname = a,username = request.user).update(close = r['data'][0]['close_yesterday'])
    #             mystock.objects.filter(stockname = a,username = request.user).update(changepct = r['data'][0]['change_pct'])
    #     return render (request,'stock/mystock.html',{})



    # def findmaxlst1():
    #     if value1samecounter >= value1upcounter and value1samecounter >= value1downcounter:
    #         return 1
    #     elif value1upcounter >= value1samecounter and value1upcounter >= value1downcounter:
    #         return 2
    #     else:
    #         return 0
    #
    #
    # def findmaxlst2():
    #     if value2samecounter >= value2upcounter and value2samecounter >= value2downcounter:
    #         return 1
    #     elif value2upcounter >= value2samecounter and value2upcounter >= value2downcounter:
    #         return 2
    #     else:
    #         return 0
    #
    # predictorvalue1 = findmaxlst1()
    # predictorvalue2 = findmaxlst2()

    # le = preprocessing.LabelEncoder()
    # a = le.fit_transform(value1)
    # b = le.fit_transform(value2)
    # labelleddata = le.fit_transform(value)
    #
    # features=list(zip(a,b))
    #
    # X_train, X_test, y_train, y_test = train_test_split(features, labelleddata, test_size=0.3,random_state=109)
    # gnb = GaussianNB()
    # gnb.fit(X_train, y_train)
    # y_pred = gnb.predict(X_test)
    #
    # var = str(gnb.predict([[predictorvalue1,predictorvalue2]]))
    # probabilties = gnb.predict_proba([[predictorvalue1,predictorvalue2]])

    # def results(var):
    #     if var == '[1]':
    #         a = 'stock close price is likely to increase with a probability of'
    #         b = str(probabilties[0][1])
    #         c = a + b
    #         return c
    #         #print(stockname + ' stock close price is likely to increase with a probability of ' + str(probabilties[0][1]))
    #     elif var =='[2]':
    #         a = ' stock close price is likely to stay the same with a probability of '
    #         b = str(probabilties[0][2])
    #         c = a + b
    #         return c
    #         #print(stockname + ' stock close price is likely to stay the same with a probability of ' + str(probabilties[0][2]))
    #     else:
    #         a = ' stock close price is likely to stay the same with a probability of '
    #         b = str(probabilties[0][0])
    #         c = a + " " + b
    #         return c
            #print(stockname +  ' stock close price is likely to go down with a probability of ' + str(probabilties[0][0]))
# new
# url = 'https://api.worldtradingdata.com/api/v1/history'
# params = {
#   'symbol': stockname,
#   'api_token': 'tsNxMjm41n3RocYkyWfIgB6xk1Z1RRahzAjzJk3pY6yQv8LR8h90kBonygk5',
#   'date_from': startdates,
#     'date_to':  enddates
#
# }
# response = requests.request('GET', url, params=params)
# a = response.json()
#
# searchresults.objects.filter(company_name = companyname).update(field = a)
#qs = searchresults.objects.filter(company_name = companyname).values('field')
# stockdetail = searchresults.objects.get(company_name = companyname)
# json_data = stockdetail.field
#print(json_data)
#print(json_data['name'])
# print(json_data['history']['2020-03-09']['open'])
# new


# for i in qs:
#     url = 'https://api.worldtradingdata.com/api/v1/history' # IF API INVALID Theier is a mistake om the history
#     params = {
#       'symbol': i.symbol,
#       'api_token': 'tsNxMjm41n3RocYkyWfIgB6xk1Z1RRahzAjzJk3pY6yQv8LR8h90kBonygk5',
#       'date_from': startdates,
#         'date_to':  enddates
#
#     }
#     response = requests.request('GET', url, params=params)
#     a = response.json()
#
#     print(i.symbol)
#     searchresults.objects.filter(symbol = i.symbol).update(field = a)










# Create your views here.
# @csrf_exempt
# def retrievestockinfo(request):
#         # Machine learning variables
#         # actualvalue = 13
#         # specialvalue2 = 2
#         closeprices = []
#         openprices = []
#         highprices = []
#         volume = []
#
#         value = []
#         value1 = []
#         value2 = []
#         value3 =[]
#
#         value1samecounter = 0
#         value1upcounter = 0
#         value1downcounter = 0
#
#         value2samecounter = 0
#         value2upcounter = 0
#         value2downcounter = 0
#
#         value3samecounter = 0
#         value3upcounter = 0
#         value3downcounter = 0
#
#         currentClosePrice = 0
#         currentOpenPrice = 0
#         currentHighPrice = 0
#         currentVolume = 0
#
#         totallength = 0
#         # Machine learning variables
#
#
#
#
#         datastore = []
#         dates = []
#         #startdates = date(2020, 1, 1)
#         #enddates = date(2020, 2, actualvalue + specialvalue2)
#         startdates = ''
#         enddates = ''
#         count = 0
#         companyname = ''
#         description = ''
#         countersss = 0
#
#         if request.method == 'POST':
#
#             a = request.POST.get('startDate')
#             b = request.POST.get('endDate')
#             startdates = datetime.strptime(a, "%Y-%m-%d")
#             enddates = datetime.strptime(b, "%Y-%m-%d")
#
#
#
#
#             # Used for updating the  historical stock data
#             # qs = searchresults.objects.all()
#             # for i in qs:
#             #       url = 'https://api.worldtradingdata.com/api/v1/history' # IF API INVALID Theier is a mistake om the history
#             #       params = {
#             #         'symbol': i.symbol,
#             #         'api_token': 'tsNxMjm41n3RocYkyWfIgB6xk1Z1RRahzAjzJk3pY6yQv8LR8h90kBonygk5',
#             #         'date_from': startdates,
#             #           'date_to':  enddates
#             #
#             #       }
#             #       response = requests.request('GET', url, params=params)
#             #       a = response.json()
#             #       searchresults.objects.filter(symbol = i.symbol).update(field = a)
#             #       print(i)
#
#             details = {
#                 'symbol':'',
#                 'name': '',
#                 'currentprice':'',
#                 'open': '',
#                 'high': '',
#                 'low': '',
#                 'close': '',
#                 'volume': '',
#
#                 'currency': '',
#                 'changepercentage': '',
#                 'volumeaverage': '',
#                 'shares': '',
#                 'time': '',
#                 'timezone': '',
#                 'timezonename': '',
#
#                 '52high': '',
#                 '52low': '',
#                 'description': '',
#
#                 'dates': '',
#                 'datastore': '',
#                 'estimate': ''
#             }
#
#             def daterange(startdates, enddates): # is two days above the date
#                 for n in range(int ((enddates - startdates).days)):
#                     yield startdates + timedelta(n)
#
#
#             stockname = request.POST.get('stockname')
#             defaultstockname = stockname
#
#             qs = searchresults.objects.all()
#
#             for i in qs:
#                 if stockname == i.company_name:
#                     companyname = i.company_name
#                     stockname = i.symbol
#                     description = i.description
#                     break
#             else:
#                 stockname = 'AAL.L'
#                 companyname = 'Anglo American plc'
#                 description = "Anglo American plc, together with its subsidiaries, engages in exploring, mining, and processing various metals and minerals worldwide. The company explores for rough and polished diamonds, copper, platinum group metals, metallurgical and thermal coal, and iron; and nickel and manganese ores, as well as alloys. Anglo American plc was founded in 1917 and is headquartered in London, the United Kingdom."
#
#             try:
                try:
                    url = 'https://api.worldtradingdata.com/api/v1/history'
                    params = {
                      'symbol': stockname,
                      'api_token': 'tsNxMjm41n3RocYkyWfIgB6xk1Z1RRahzAjzJk3pY6yQv8LR8h90kBonygk5',
                      'date_from': startdates,
                        'date_to':  enddates

                    }
                    response = requests.request('GET', url, params=params)
                    a = response.json()

                    if a:
                        searchresults.objects.filter(company_name = companyname).update(field = a)
                    else:
                        raise
#                 #
#                 #
#                 #     #searchresults.objects.filter(company_name = companyname).update(field = a)
#                 #     for single_date in daterange(startdates, enddates):
#                 #         #print(single_date.strftime("%Y-%m-%d"))
#                 #        try:
#                 #           closeprices.append(a['history'][single_date.strftime("%Y-%m-%d")]['close'])
#                 #           openprices.append(a['history'][single_date.strftime("%Y-%m-%d")]['open'])
#                 #           highprices.append(a['history'][single_date.strftime("%Y-%m-%d")]['high'])
#                 #           volume.append(a['history'][single_date.strftime("%Y-%m-%d")]['volume'])
#                 #           dates.append(single_date.strftime("%Y-%m-%d"))
#                 #           #print(a['history'][single_date.strftime("%Y-%m-%d")]['close'] + " " +  single_date.strftime("%Y-%m-%d"))
#                 #        except:
#                 #             pass
#                 # except:
#                 print("Exception Field")
#                 stockdetail = searchresults.objects.get(company_name = companyname)
#                 json_data = stockdetail.field
#                 for single_date in daterange(startdates, enddates):
#                     #print(single_date.strftime("%Y-%m-%d"))
#                    try:
#                       closeprices.append(json_data['history'][single_date.strftime("%Y-%m-%d")]['close'])
#                       openprices.append(json_data['history'][single_date.strftime("%Y-%m-%d")]['open'])
#                       highprices.append(json_data['history'][single_date.strftime("%Y-%m-%d")]['high'])
#                       volume.append(json_data['history'][single_date.strftime("%Y-%m-%d")]['volume'])
#                       dates.append(single_date.strftime("%Y-%m-%d"))
#                       #print(a['history'][single_date.strftime("%Y-%m-%d")]['close'] + " " +  single_date.strftime("%Y-%m-%d"))
#                    except:
#                         pass
#
#                 for i in range(len(closeprices)):
#                     if i == 0:
#                         currentClosePrice = closeprices[i]
#                         value.append('same')
#
#                     elif closeprices[i] > currentClosePrice:
#                         currentClosePrice = closeprices[i]
#                         value.append('increase')
#
#                     elif closeprices[i] == currentClosePrice:
#                          currentClosePrice = closeprices[i]
#                          value.append('same')
#                     else:
#                         value.append('decrease')
#                         currentClosePrice = closeprices[i]
#
#                 for i in range(len(openprices)):
#                     if i == 0:
#                         currentOpenPrice = openprices[i]
#                         value1.append('same')
#                         value1samecounter+=1
#
#                     elif openprices[i] > currentOpenPrice:
#                         currentOpenPrice = openprices[i]
#                         value1.append('up')
#                         value1upcounter+=1
#
#                     elif openprices[i] == currentOpenPrice:
#                          currentOpenPrice = openprices[i]
#                          value1.append('same')
#                          value1samecounter+=1
#
#                     else:
#                         value1.append('down')
#                         currentOpenPrice = openprices[i]
#                         value1downcounter+=1
#
#                 for i in range(len(highprices)):
#                     if i == 0:
#                         currentHighPrice = highprices[i]
#                         value2.append('same')
#                         value2samecounter+=1
#
#                     elif highprices[i] > currentHighPrice:
#                          currentHighPrice = highprices[i]
#                          value2.append('up')
#                          value2upcounter+=1
#
#                     elif highprices[i] == currentHighPrice:
#                          currentHighPrice = highprices[i]
#                          value2.append('same')
#                          value2samecounter+=1
#
#                     else:
#                         value2.append('down')
#                         currentHighPrice = highprices[i]
#                         value2downcounter+=1
#
#                 for i in range(len(volume)):
#                     if i == 0:
#                         currentVolume = volume[i]
#                         value3.append('same')
#                         value3samecounter+=1
#
#                     elif volume[i] > currentHighPrice:
#                          currentVolume = volume[i]
#                          value3.append('up')
#                          value3upcounter+=1
#
#                     elif highprices[i] == currentHighPrice:
#                          currentVolume = volume[i]
#                          value3.append('same')
#                          value3samecounter+=1
#
#                     else:
#                         value3.append('down')
#                         currentVolume = volume[i]
#                         value3downcounter+=1
#
#                 def findmaxlst(a,b,c): # only done on features
#
#                     if a >= b and a >= c:
#                         return 1
#                     elif b >= a and b >= c:
#                         return 2
#                     else:
#                         return 0
#
#                 predictorvalue1 = findmaxlst(value1samecounter,value1upcounter,value1downcounter)
#                 predictorvalue2 = findmaxlst(value2samecounter,value2upcounter,value2downcounter)
#                 predictorvalue3 = findmaxlst(value3samecounter,value3upcounter,value3downcounter)
#
#
#                 le = preprocessing.LabelEncoder()
#                 a = le.fit_transform(value1)
#                 b = le.fit_transform(value2)
#                 c = le.fit_transform(value3)
#
#                 labelleddata = le.fit_transform(value)
#
#                 features=list(zip(a,b,c))
#
#                 X_train, X_test, y_train, y_test = train_test_split(features, labelleddata, test_size=0.3,random_state=109)
#                 # 0.3
#                 # print(X_train)
#                 # print(X_test)
#                 # print(y_train)
#                 # print(y_test)
#                 gnb = MultinomialNB()
#                 gnb.fit(X_train, y_train)
#                 y_pred = gnb.predict(X_test)
#
#
#                 var = str(gnb.predict([[predictorvalue1,predictorvalue2,predictorvalue3]]))
#                 probabilties = gnb.predict_proba([[predictorvalue1,predictorvalue2,predictorvalue3]])
#
#
#                 def results(var):
#                     if var == '[1]':
#                         v = stockname + ' stock close price is likely to go up with a probability of ' + str(int(probabilties[0][1] * 100)) + '%'
#                         return v
#                     elif var =='[2]':
#                         v = stockname + ' stock close price is likely to stay the same with a probability of ' + str(int(probabilties[0][2] * 100)) + '%'
#                         return v
#                     else:
#                         v = stockname +  ' stock close price is likely to go down with a probability of ' + str(int(probabilties[0][0] * 100)) + '%'
#                         return v
#
#
#
#                 calculations = results(var)
#                 print(calculations)
#                 # Machine learning
#
#                 stock = '{}'.format(stockname)
#
#                 for i in range(len(closeprices)):
#                     datastore.append(closeprices[i])
#
#
#
#
#
                # try:
                #     r = requests.get('https://api.worldtradingdata.com/api/v1/stock?symbol={}&api_token=tsNxMjm41n3RocYkyWfIgB6xk1Z1RRahzAjzJk3pY6yQv8LR8h90kBonygk5'.format(stock)).json()
                #     #searchresults.objects.filter(company_name = companyname).update(field1 = r) # important
                #     if r:
                #         searchresults.objects.filter(company_name = companyname).update(field1 = r) # important
                #     else:
                #
                #         raise
#                 #
#                 #     details = {
#                 #         'symbol':r['data'][0]['symbol'],
#                 #         'name': r['data'][0]['name'],
#                 #         'currentprice':r['data'][0]['price'],
#                 #         'open': r['data'][0]['price_open'],
#                 #         'high': r['data'][0]['day_high'],
#                 #         'low': r['data'][0]['day_low'],
#                 #         'close': r['data'][0]['close_yesterday'],
#                 #         'volume': r['data'][0]['volume'],
#                 #
#                 #         'currency': r['data'][0]['currency'],
#                 #         'changepercentage': r['data'][0]['change_pct'],
#                 #         'volumeaverage': r['data'][0]['volume_avg'],
#                 #         'shares': r['data'][0]['shares'],
#                 #         'time': r['data'][0]['last_trade_time'],
#                 #         'timezone': r['data'][0]['timezone'],
#                 #         'timezonename': r['data'][0]['timezone_name'],
#                 #
#                 #         '52high': r['data'][0]['52_week_high'],
#                 #         '52low': r['data'][0]['52_week_low'],
#                 #         'description': description,
#                 #
#                 #         'dates': dates,
#                 #         'datastore': datastore,
#                 #         'estimate': calculations
#                 #         }
#                 # except:
#                 print("Exception field1")
#                 stockdetails = searchresults.objects.get(company_name = companyname)
#                 json_datas = stockdetails.field1
#
#                 details = {
#                     'symbol':json_datas['data'][0]['symbol'],
#                     'name': json_datas['data'][0]['name'],
#                     'currentprice':json_datas['data'][0]['price'],
#                     'open': json_datas['data'][0]['price_open'],
#                     'high': json_datas['data'][0]['day_high'],
#                     'low': json_datas['data'][0]['day_low'],
#                     'close': json_datas['data'][0]['close_yesterday'],
#                     'volume': json_datas['data'][0]['volume'],
#
#                     'currency': json_datas['data'][0]['currency'],
#                     'changepercentage': json_datas['data'][0]['change_pct'],
#                     'volumeaverage': json_datas['data'][0]['volume_avg'],
#                     'shares': json_datas['data'][0]['shares'],
#                     'time': json_datas['data'][0]['last_trade_time'],
#                     'timezone': json_datas['data'][0]['timezone'],
#                     'timezonename': json_datas['data'][0]['timezone_name'],
#
#                     '52high': json_datas['data'][0]['52_week_high'],
#                     '52low': json_datas['data'][0]['52_week_low'],
#                     'description': description,
#
#                     'dates': dates,
#                     'datastore': datastore,
#                     'estimate': calculations
#                     }
#
#             except:
#                 pass
#             return JsonResponse(details)
#         else:
#             return render (request,'stock/stockinformation.html',{})
#
#
#
#
#
#
#
#
#
#
#










#
# @csrf_exempt
# @login_required
# def mystockinfo(request):
#
#     # Used for updating the Real Time stock data
#
#     # qs = searchresults.objects.all()
#     # for i in qs:
#     #     stock = '{}'.format(i.symbol)
#     #     #print(stock)
#     #     r = requests.get('https://api.worldtradingdata.com/api/v1/stock?symbol={}&api_token=tsNxMjm41n3RocYkyWfIgB6xk1Z1RRahzAjzJk3pY6yQv8LR8h90kBonygk5'.format(stock)).json()
#     #     searchresults.objects.filter(symbol = i.symbol).update(field1 = r) # important
#     #
#     #
#     #     searchresults.objects.filter(symbol = i.symbol).update(field1 = r) # important
#     #     print("update")
#
#     qs = mystock.objects.all()
#
#     for i in qs:
#         addmystockinfoss(request,i.stockname)
#     queryset = mystock.objects.filter(username = request.user)
#     context = {
#         'object_list' : queryset
#     }
#     return render (request,'stock/mystock.html',context)







# @csrf_exempt
# def addmystockinfoss(request,stockname):
#     a = stockname
#     # try:
#     #     r = requests.get('https://api.worldtradingdata.com/api/v1/stock?symbol={}&api_token=tsNxMjm41n3RocYkyWfIgB6xk1Z1RRahzAjzJk3pY6yQv8LR8h90kBonygk5'.format(a)).json()
#     #     if r:
#     #         if mystock.objects.filter(stockname = a,username = request.user).exists():
#     #             mystock.objects.filter(stockname = a,username = request.user).update(volume = r['data'][0]['volume'])
#     #             mystock.objects.filter(stockname = a,username = request.user).update(open = r['data'][0]['price_open'])
#     #             mystock.objects.filter(stockname = a,username = request.user).update(high = r['data'][0]['day_high'])
#     #             mystock.objects.filter(stockname = a,username = request.user).update(low = r['data'][0]['day_low'])
#     #             mystock.objects.filter(stockname = a,username = request.user).update(close = r['data'][0]['close_yesterday'])
#     #             mystock.objects.filter(stockname = a,username = request.user).update(changepct = r['data'][0]['change_pct'])
#     #             mystock.objects.filter(stockname = a,username = request.user).update(name = r['data'][0]['name'])
#     #     else:
#     #         raise
#     # except:
#     #print('ehllo')
#     stockdet = searchresults.objects.get(symbol = stockname)
#     json_datas1 = stockdet.field1
#     if mystock.objects.filter(stockname = a,username = request.user).exists():
#         mystock.objects.filter(stockname = a,username = request.user).update(volume = json_datas1['data'][0]['volume'])
#         mystock.objects.filter(stockname = a,username = request.user).update(open = json_datas1['data'][0]['price_open'])
#         mystock.objects.filter(stockname = a,username = request.user).update(high = json_datas1['data'][0]['day_high'])
#         mystock.objects.filter(stockname = a,username = request.user).update(low = json_datas1['data'][0]['day_low'])
#         mystock.objects.filter(stockname = a,username = request.user).update(close = json_datas1['data'][0]['close_yesterday'])
#         mystock.objects.filter(stockname = a,username = request.user).update(changepct = json_datas1['data'][0]['change_pct'])
#         mystock.objects.filter(stockname = a,username = request.user).update(name = json_datas1['data'][0]['name'])
#     return







#                 // var stockcompanies = [
#                 //             "Anglo American plc",
#                 //             "Associated British Foods plc",
#                 //             "Admiral Group plc",
#                 //             "Ashtead Group plc",
#                 //             "Antofagasta plc",
#                 //             "Auto Trader Group PLC",
#                 //             "Aviva plc",
#                 //             "AVEVA Group plc",
#                 //             "AstraZeneca plc",
#                 //             "BAE Systems plc",
#                 //             "Barclays PLC",
#                 //             "BRITISH AMERICAN TOBACCO PLC ADS Common Stock",
#                 //             "LSE London Stock Exchange Plc",
#                 //             "Barratt Developments Plc",
#                 //             "Berkeley Group Holdings PLC",
#                 //             "British Land Company PLC",
#                 //             "Bunzl plc",
#                 //             "BP plc",
#                 //             "Burberry Group plc",
#                 //             "BHP Group PLC",
#                 //             "BT Group - CLASS A Common Stock",
#                 //             "Coca Cola HBC AG",
#                 //             "Carnival Corporation & Plc",
#                 //             "Centrica PLC",
#                 //             "Compass Group plc",
#                 //             "Croda International Plc",
#                 //             "CRH PLC",
#                 //             "DCC plc",
#                 //             "Diageo plc",
#                 //             "EVRAZ plc",
#                 //             "Experian plc",
#                 //             "easyJet plc",
#                 //             "Ferguson PLC",
#                 //             "Flutter Entertainment PLC",
#                 //             "Glencore PLC",
#                 //             "GlaxoSmithKline plc",
#                 //             "Hikma Pharmaceuticals Plc",
#                 //             "Hargreaves Lansdown PLC",
#                 //             "Halma plc",
#                 //             "HSBC Holdings plc",
#                 //             "International Consolidated Airlns Grp SA",
#                 //             "INTERCONTINENTAL HOTELS GROUP Common Stock",
#                 //             "3i Group plc",
#                 //             "Imperial Brands PLC",
#                 //             "Informa PLC",
#                 //             "Intertek Group plc",
#                 //             "ITV plc",
#                 //             "JD Sports Fashion PLC",
#                 //             "Just Eat Takeaway.com NV",
#                 //             "Johnson Matthey PLC",
#                 //             "Land Securities Group plc",
#                 //             "Legal & General Group Plc",
#                 //             "Lloyds Banking Group PLC",
#                 //             "Meggitt plc",
#                 //             "Mondi Plc",
#                 //             "M&G PLC",
#                 //             "Melrose Industries PLC",
#                 //             "WM Morrison Supermarkets PLC",
#                 //             "National Grid plc",
#                 //             "NEXT plc",
#                 //             "Ocado Group PLC",
#                 //             "Phoenix Group Holdings",
#                 //             "Pennon Group plc",
#                 //             "Polymetal International PLC",
#                 //             "Prudential plc",
#                 //             "Persimmon plc",
#                 //             "Pearson plc",
#                 //             "Reckitt Benckiser Group Plc",
#                 //             "Royal Bank of Scotland Group plc",
#                 //             "Royal Dutch Shell Plc",
#                 //             "Royal Dutch Shell Plc Class B",
#                 //             "Relx PLC",
#                 //             "Rio Tinto plc",
#                 //             "Rightmove Plc",
#                 //             "Rolls-Royce Holding PLC",
#                 //             "RSA Insurance Group plc",
#                 //             "Rentokil Initial plc",
#                 //             "J Sainsbury plc",
#                 //             "SCHRODERS/PAR VTG FPD 1",
#                 //             "The Sage Group plc",
#                 //             "SEGRO plc",
#                 //             "Smurfit Kappa Group Plc",
#                 //             "Standard Life Aberdeen PLC",
#                 //             "DS Smith plc",
#                 //             "Smiths Group plc",
#                 //             "Scottish Mortgage Investment Trust PLC",
#                 //             "Smith & Nephew plc",
#                 //             "Spirax-Sarco Engineering plc",
#                 //             "SSE PLC",
#                 //             "Standard Chartered PLC",
#                 //             "St. James Place plc",
#                 //             "Severn Trent Plc",
#                 //             "Tesco PLC",
#                 //             "Taylor Wimpey plc",
#                 //             "Unilever plc",
#                 //             "United Utilities Group PLC",
#                 //             "Vodafone Group plc",
#                 //             "WPP PLC",
#                 //             "Whitbread plc"
#                 //         ];
# //                 function autocomplete(inp, arr) {
# //                   /*the autocomplete function takes two arguments,
# //                   the text field element and an array of possible autocompleted values:*/
# //                   var currentFocus;
# //                   /*execute a function when someone writes in the text field:*/
# //                   inp.addEventListener("input", function(e) {
# //                   var a, b, i, val = this.value;
# //                   /*close any already open lists of autocompleted values*/
# //                   closeAllLists();
# //                   if (!val) { return false;}
# //                   currentFocus = -1;
# //                   /*create a DIV element that will contain the items (values):*/
# //                   a = document.createElement("DIV");
# //                   a.setAttribute("id", this.id + "autocomplete-list");
# //                   a.setAttribute("class", "autocomplete-items");
# //                   /*append the DIV element as a child of the autocomplete container:*/
# //                   this.parentNode.appendChild(a);
# //                   /*for each item in the array...*/
# //                   for (i = 0; i < arr.length; i++) {
# //                     /*check if the item starts with the same letters as the text field value:*/
# //                     if (arr[i].substr(0, val.length).toUpperCase() == val.toUpperCase()) {
# //                       /*create a DIV element for each matching element:*/
# //                       b = document.createElement("DIV");
# //                       /*make the matching letters bold:*/
# //                       b.innerHTML = "<strong>" + arr[i].substr(0, val.length) + "</strong>";
# //                       b.innerHTML += arr[i].substr(val.length);
# //                       /*insert a input field that will hold the current array item's value:*/
# //                       b.innerHTML += "<input type='hidden' value='" + arr[i] + "'>";
# //                       /*execute a function when someone clicks on the item value (DIV element):*/
# //                           b.addEventListener("click", function(e) {
# //                           /*insert the value for the autocomplete text field:*/
# //                           inp.value = this.getElementsByTagName("input")[0].value;
# //                           /*close the list of autocompleted values,
# //                           (or any other open lists of autocompleted values:*/
# //                           closeAllLists();
# //                       });
# //                       a.appendChild(b);
# //                     }
# //                   }
# //             });
# //   /*execute a function presses a key on the keyboard:*/
# //   inp.addEventListener("keydown", function(e) {
# //       var x = document.getElementById(this.id + "autocomplete-list");
# //       if (x) x = x.getElementsByTagName("div");
# //       if (e.keyCode == 40) {
# //         /*If the arrow DOWN key is pressed,
# //         increase the currentFocus variable:*/
# //         currentFocus++;
# //         /*and and make the current item more visible:*/
# //         addActive(x);
# //       } else if (e.keyCode == 38) { //up
# //         /*If the arrow UP key is pressed,
# //         decrease the currentFocus variable:*/
# //         currentFocus--;
# //         /*and and make the current item more visible:*/
# //         addActive(x);
# //       } else if (e.keyCode == 13) {
# //         /*If the ENTER key is pressed, prevent the form from being submitted,*/
# //         e.preventDefault();
# //         if (currentFocus > -1) {
# //           /*and simulate a click on the "active" item:*/
# //           if (x) x[currentFocus].click();
# //         }
# //       }
# //   });
# //   function addActive(x) {
# //     /*a function to classify an item as "active":*/
# //     if (!x) return false;
# //     /*start by removing the "active" class on all items:*/
# //     removeActive(x);
# //     if (currentFocus >= x.length) currentFocus = 0;
# //     if (currentFocus < 0) currentFocus = (x.length - 1);
# //     /*add class "autocomplete-active":*/
# //     x[currentFocus].classList.add("autocomplete-active");
# //   }
# //   function removeActive(x) {
# //     /*a function to remove the "active" class from all autocomplete items:*/
# //     for (var i = 0; i < x.length; i++) {
# //       x[i].classList.remove("autocomplete-active");
# //     }
# //   }
# //   function closeAllLists(elmnt) {
# //     /*close all autocomplete lists in the document,
# //     except the one passed as an argument:*/
# //     var x = document.getElementsByClassName("autocomplete-items");
# //     for (var i = 0; i < x.length; i++) {
# //       if (elmnt != x[i] && elmnt != inp) {
# //       x[i].parentNode.removeChild(x[i]);
# //     }
# //   }
# // }
# // /*execute a function when someone clicks in the document:*/
# // document.addEventListener("click", function (e) {
# //     closeAllLists(e.target);
# // });
# // }
#                  // autocomplete(document.getElementById("search"), stockcompanies);
#




# /* * { box-sizing: border-box; }
# body {
#   font: 16px Arial;
# }
# .autocomplete {
#   position: relative;
#   display: inline-block;
# }
# input {
#   border: 1px solid transparent;
#   background-color: #f1f1f1;
#   padding: 10px;
#   font-size: 16px;
# }
# input[type=text] {
#   background-color: #f1f1f1;
#   width: 100%;
# }
# input[type=submit] {
#
#   color: #fff;
#
# }
# .autocomplete-items {
#   position: absolute;
#   border: 1px solid #d4d4d4;
#   border-bottom: none;
#   border-top: none;
#   z-index: 99;
#   top: 100%;
#   left: 0;
#   right: 0;
# }
# .autocomplete-items div {
#   padding: 10px;
#   cursor: pointer;
#   background-color: #fff;
#   border-bottom: 1px solid #d4d4d4;
# }
# .autocomplete-items div:hover {
#
#   background-color: #e9e9e9;
# }
# .autocomplete-active {
#
#
#   color: #ffffff;
# }
#
# .btn-primary:hover{
# background-color: #8064A2 !important;
# outline: none !important;
#  box-shadow: none !important;
# } */






# .scroll {
#         max-height: 200px;
#         overflow-y: auto;
#     }
# .form-control-borderless {
# border: none;
# }
# .form-control-borderless:hover, .form-control-borderless:active, .form-control-borderless:focus {
#     border: none;
#     outline: none;
#     box-shadow: none;
# }
# ::-webkit-input-placeholder { /* Chrome/Opera/Safari */
#       font-style: italic;
# }
# ::-moz-placeholder { /* Firefox 19+ */
#     font-style: italic;
# }
# :-ms-input-placeholder { /* IE 10+ */
#     font-style: italic;
# }
# :-moz-placeholder { /* Firefox 18- */
#     font-style: italic;
# }
# .container-main {
# margin-top: 75px;
# }
