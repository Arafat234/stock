from django.test import TestCase, Client
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.urls import path, include, reverse, resolve
from stocksearch.models import *
import jsonfield


# python manage.py test stocksearch/test

class Testsearchresult(TestCase):


    def create_search(self, u, e, p, f, l):
        return searchresults.objects.create(company_name=u, symbol=e, field=p, field1=f, description=l)



    def setUp(self):
        self.field = { "name": "WPP.L", "history": { "2020-04-01": { "open": "528.00", "close": "493.30", "high": "536.80", "low": "489.60", "volume": "7516764" }, "2020-03-31": { "open": "522.20", "close": "551.40", "high": "562.80", "low": "493.30", "volume": "13228442" }, } }
        self.field1 = { "symbols_requested": 1, "symbols_returned": 1, "data": [ { "symbol": "WPP.L", "name": "WPP PLC", "currency": "GBX", "price": "483.70", "price_open": "509.40", "day_high": "520.04", "day_low": "481.30", "52_week_high": "1085.50", "52_week_low": "450.00", "day_change": "-32.30", "change_pct": "-6.26", "close_yesterday": "516.00", "market_cap": "35718339882", "volume": "4463493", "volume_avg": "8768025", "shares": "1225329072", "stock_exchange_long": "London Stock Exchange", "stock_exchange_short": "LSE", "timezone": "BST", "timezone_name": "Europe/London", "gmt_offset": "3600", "last_trade_time": "2020-04-03 16:35:18", "pe": "9.71", "eps": "0.50" } ] }
        newsearchresult = self.create_search("WPP PLC", "WPP.L", self.field,self.field1, "hello")

    def tearDown(self):
        searchresults.objects.all().delete()

    def test_searchresult_attributes(self): # test whether attributes are stored in database
        company = searchresults.objects.get(company_name="WPP PLC")
        self.assertEqual(company.symbol,"WPP.L")
        self.assertEqual(company.field,self.field)
        self.assertEqual(company.field1,self.field1)
        self.assertEqual(company.description,"hello")

    def test_searchresult_exist(self): # test for unique user
        num_results = searchresults.objects.filter(company_name="WPP PLC").count()
        self.assertEqual(1,num_results)


    def test_update_db(self): # Obtains object with user and proceeds to update profile
        company = searchresults.objects.get(company_name="WPP PLC")
        somevariable = { "name": "WPP.L", "history": { "2020-04-01": { "open": "520.00", "close": "493.30", "high": "536.80", "low": "489.60", "volume": "7516764" }, "2020-03-31": { "open": "522.20", "close": "550.40", "high": "560.80", "low": "490.30", "volume": "13228442" }, } }
        company.field = somevariable
        somevariable2 = { "symbols_requested": 1, "symbols_returned": 1, "data": [ { "symbol": "WPA.L", "name": "WPP PLC", "currency": "GBX", "price": "483.70", "price_open": "500.40", "day_high": "520.04", "day_low": "481.30", "52_week_high": "1085.50", "52_week_low": "450.00", "day_change": "-32.30", "change_pct": "-6.26", "close_yesterday": "516.00", "market_cap": "35718339882", "volume": "4463493", "volume_avg": "8768025", "shares": "1225329072", "stock_exchange_long": "London Stock Exchange", "stock_exchange_short": "LSE", "timezone": "BST", "timezone_name": "Europe/London", "gmt_offset": "3600", "last_trade_time": "2020-04-03 16:35:18", "pe": "9.71", "eps": "0.50" } ] }
        company.field1 = somevariable2
        company.symbol = "WPA.L"
        company.save()
        company = searchresults.objects.get(company_name="WPP PLC")
        self.assertEqual(company.field,somevariable)
        self.assertEqual(company.field1,somevariable2)
        self.assertNotEqual(company.symbol,"WPP.L")


class Testmystock(TestCase):

        def create_user(self, u, e, p, f, l):
            return User.objects.create_user(username=u, email=e, password=p, first_name=f, last_name=l)


        def setUp(self):
            newuser = self.create_user("arafat64", "arafat64@outlook.com", "abir1234", "", "")
            newstock = mystock.objects.create(username= newuser,stockname = 'WPP PLC',volume = '10',open='200',high='300',low='300',close='200',changepct = '5',name='WPP PLC')

        def tearDown(self):
            mystock.objects.all().delete()
            User.objects.all().delete()

        def test_searchresult_attributes(self): # test whether attributes are stored in database
            stocknames = mystock.objects.get(stockname='WPP PLC')
            self.assertNotEqual(stocknames.stockname,"WPP.L")
            self.assertEqual(stocknames.volume,'10')
            self.assertEqual(stocknames.open,'200')
            self.assertEqual(stocknames.high,'300')
            self.assertEqual(stocknames.low,'300')
            self.assertEqual(stocknames.close,'200')
            self.assertEqual(stocknames.changepct,'5')
            self.assertEqual(stocknames.name,'WPP PLC')


        def test_update_db(self): # Obtains object with user and proceeds to update profile
            stocknames = mystock.objects.get(stockname='WPP PLC')
            stocknames.open = '300'
            stocknames.high = '500'
            stocknames.low = '400'
            stocknames.close = '500'
            stocknames.volume = '15'
            stocknames.save()
            stocknames = mystock.objects.get(stockname='WPP PLC')
            self.assertEqual(stocknames.open,'300')
            self.assertEqual(stocknames.high,'500')
            self.assertEqual(stocknames.low,'400')
            self.assertEqual(stocknames.close,'500')
            self.assertEqual(stocknames.volume,'15')


class Testnews(TestCase):
        def setUp(self):
            newnews = news.objects.create(name='donald',newsfield = {'date' : '06/04/98','article' : 'usa news'})

        def tearDown(self):
            news.objects.all().delete()

        def test_news_attributes(self):
            newss = news.objects.get(name='donald')
            self.assertEqual(newss.newsfield['date'],'06/04/98')
            self.assertEqual(newss.newsfield['article'],'usa news')

        def test_update_db(self): # Obtains object with user and proceeds to update profile
            newss = news.objects.get(name='donald')
            newss.newsfield['date'] = '06/03/10'
            newss.newsfield['article'] = 'england news'
            newss.save()
            newss = news.objects.get(name='donald')
            self.assertEqual(newss.newsfield['date'],'06/03/10')
            self.assertEqual(newss.newsfield['article'],'england news')
