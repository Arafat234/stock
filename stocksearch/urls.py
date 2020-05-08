from django.contrib import admin
from django.urls import path, include
from .views import retrievestockinfo,addstockinfo,mystockinfo,deletemystockinfo,newsinfo
urlpatterns = [
    path('',retrievestockinfo, name='stockinfo'),
    path('addstockinfo/',addstockinfo, name='addstockinfos'),
    path('mystock/',mystockinfo, name='mystockinfos'),
    path('deletemystock/',deletemystockinfo, name='deletemystockinfo'),
    path('news/',newsinfo, name='newsinfo'),

]
