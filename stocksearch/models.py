from django.db import models
from django.contrib.auth.models import User
import jsonfield
# Create your models here.
class searchresults(models.Model):
     company_name = models.TextField(null=True,blank=True)
     symbol = models.TextField(null=True,blank=True)
     field = jsonfield.JSONField(null=True, blank=True)
     field1 = jsonfield.JSONField(null=True, blank=True)
     description = models.TextField(null=True,blank=True)

class mystock(models.Model):
     username = models.ForeignKey(User,null=True,on_delete=models.CASCADE)
     stockname = models.TextField(null=True,blank=True)
     volume = models.TextField(null=True,blank=True)
     open =  models.TextField(null=True,blank=True)
     high =  models.TextField(null=True,blank=True)
     low =  models.TextField(null=True,blank=True)
     close =  models.TextField(null=True,blank=True)
     changepct =  models.TextField(null=True,blank=True)
     name =  models.TextField(null=True,blank=True)

class news(models.Model):
    name = models.TextField(null=True,blank=True)
    newsfield = jsonfield.JSONField(null=True, blank=True)
