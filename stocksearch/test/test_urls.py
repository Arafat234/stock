from django.test import TestCase, Client
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.urls import path, include, reverse, resolve
from datetime import datetime as dt, date
from stocksearch.models import *
from stocksearch.views import *
import jsonfield


# python manage.py test mainapp/tests

class Testurls(TestCase):

    def create_user(self, u, e, p, f, l):
        return User.objects.create_user(username=u, email=e, password=p, first_name=f, last_name=l)

    def setUp(self):
        self.client = Client()
        newuser = self.create_user("arafat64", "arafat64@outlook.com", "abir1234", "", "")
        newss = news.objects.create(name='one',newsfield = {'date':'06/04/10','article':'uk news'})
        # newprofile = self.createprofile(newuser)
        # return

    def tearDown(self):
        User.objects.all().delete()
        news.objects.all().delete()



    def test_retrievestockinfo(self): # check if home function is triggered with right home template and return the correct response code and displays the appropriate url name
        url = reverse("stockinfo")
        self.assertEqual(resolve(url).func,retrievestockinfo)
        self.assertEqual(resolve(url).url_name, "stockinfo")
        response = self.client.get(reverse('stockinfo'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'stock/stockinformation.html')


    def test_addstockinfo(self): # check if help function is triggered with right help template and return the correct response code and displays the appropriate url name
        url = reverse("addstockinfos")
        self.assertEqual(resolve(url).func,addstockinfo)
        self.assertEqual(resolve(url).url_name, "addstockinfos")
        payload = {"stockname": "WPP PLC"}
        response = self.client.post(reverse("addstockinfos"), payload, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEquals(response.status_code, 302) # The use of redirects caused a 302 response code



    def test_mystock(self): # check if signup function is triggered with right help template and return the correct response code and displays the appropriate url name
        url = reverse("mystockinfos")
        self.assertEqual(resolve(url).func,mystockinfo)
        self.assertEqual(resolve(url).url_name, "mystockinfos")
        response = self.client.get(reverse('mystockinfos'))
        self.assertEqual(response.status_code, 302)


    def test_deletemystockinfo(self): # check if viewprofile function is triggered with right viewprofile template and return the correct response code and displays the appropriate url name
        url = reverse("deletemystockinfo")
        self.assertEqual(resolve(url).func,deletemystockinfo)
        self.assertEqual(resolve(url).url_name, "deletemystockinfo")
        response = self.client.get(reverse('deletemystockinfo'))
        self.assertEqual(response.status_code, 302) # The use of redirects caused a 302 response code

    def test_news(self): # check if viewprofile function is triggered with right viewprofile template and return the correct response code and displays the appropriate url name
        url = reverse("newsinfo")
        self.assertEqual(resolve(url).func,newsinfo)
        self.assertEqual(resolve(url).url_name, "newsinfo")
        response = self.client.get(reverse('newsinfo'))
        self.assertEqual(response.status_code, 200)
