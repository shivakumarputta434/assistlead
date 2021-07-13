from django.db import models
import jsonfield
from django.utils import timezone
# Create your models here.

#Testing Model

class Testtable(models.Model):
    linkedin_url=models.CharField(max_length=250)
    company_name=models.CharField(max_length=250)

#Company Model

class Company(models.Model):
    linkedin_url=models.CharField(max_length=250)
    retrieval_date=models.DateTimeField(default=timezone.now)
    linkedin_user=models.CharField(max_length=250,blank=True)
    data=jsonfield.JSONField()


#Profile Model

class Profile(models.Model):
    linkedin_url=models.CharField(max_length=250)
    retrieval_date=models.DateTimeField(default=timezone.now)
    linkedin_user=models.CharField(max_length=250,blank=True)
    data=jsonfield.JSONField()