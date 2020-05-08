from django.test import TestCase, Client
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.urls import path, include, reverse, resolve
from users.models import *
import jsonfield


# python manage.py test users/test

class Testprofile(TestCase):

    def create_user(self, u, e, p, f, l):
        return User.objects.create_user(username=u, email=e, password=p, first_name=f, last_name=l)

    def createprofile(self,user,image):
        return user.createprofile_set.create(image)

    def setUp(self):
        newuser = self.create_user("arafat64", "arafat64@outlook.com", "abir1234", "", "")
        # newprofile = self.createprofile(newuser)
        # return

    def tearDown(self):
        User.objects.all().delete()

    def test_user_attributes(self): # test whether attributes are stored in database
        user = User.objects.get(username="arafat64")
        self.assertEqual(user.email,"arafat64@outlook.com")

    def test_user_exist(self): # test for unique user
        num_results = User.objects.filter(username="arafat64").count()
        self.assertEqual(1,num_results)

    def test_update_db(self): # Obtains object with user and proceeds to update profile
        user = User.objects.get(username="arafat64")
        user.username = "Jacob"
        user.email = "arafat81@outlook.com"
        user.save()
        user = User.objects.get(username = "Jacob")
        self.assertEqual(user.email,"arafat81@outlook.com")
