from django.db import models

# Creating a company model
class Company(models.Model):
    Company_id = models.AutoField(primary_key= True)
    name = models.CharField(max_length=100)
    active = models.BooleanField(default=True)
    location =  models.CharField(max_length=100)
    about = models.TextField()
