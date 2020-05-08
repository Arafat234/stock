from django.test import TestCase, Client
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.urls import path, include, reverse, resolve
from datetime import datetime as dt, date
from users.models import *
from users.views import *
import jsonfield


# python manage.py test users/test

class Testurls(TestCase):

    def create_user(self, u, e, p, f, l):
        return User.objects.create_user(username=u, email=e, password=p, first_name=f, last_name=l)

    def setUp(self):
        self.client = Client()
        newuser = self.create_user("arafat64", "arafat64@outlook.com", "abir1234", "", "")
        # newprofile = self.createprofile(newuser)
        # return

    def tearDown(self):
        User.objects.all().delete()

# path('', views.home, name='home')

    def test_home(self): # check if home function is triggered with right home template and return the correct response code and displays the appropriate url name
        url = reverse("home")
        self.assertEqual(resolve(url).func,home)
        self.assertEqual(resolve(url).url_name, "home")
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_help(self): # check if help function is triggered with right help template and return the correct response code and displays the appropriate url name
        url = reverse("help")
        self.assertEqual(resolve(url).func,help)
        self.assertEqual(resolve(url).url_name, "help")
        response = self.client.get(reverse('help'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'help.html')


# path('signup/', views.signup, name='signup'),

    def test_signup(self): # check if signup function is triggered with right help template and return the correct response code and displays the appropriate url name
        url = reverse("signup")
        self.assertEqual(resolve(url).func,signup)
        self.assertEqual(resolve(url).url_name, "signup")
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/signup.html')


# path('viewprofile/', views.profile, name='profile'),

    def test_viewprofile(self): # check if viewprofile function is triggered with right viewprofile template and return the correct response code and displays the appropriate url name
        url = reverse("profile")
        self.assertEqual(resolve(url).func,profile)
        self.assertEqual(resolve(url).url_name, "profile")
        response = self.client.get(reverse('profile'))
        self.assertRedirects(response, '/accounts/login/?next=/viewprofile/')
        self.assertEqual(response.status_code, 302)
