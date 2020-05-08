from django.contrib import admin
from .models import searchresults,mystock,news
# Register your models here.

admin.site.register(searchresults)
admin.site.register(mystock)
admin.site.register(news)
