from django.db import models

# Create your models here.

class Destination(models.Model):
	name = models.CharField(max_length=100)
	img = models.CharField(max_length=100) #ImageField(upload_to='pics') #TextField() 
	desc = models.TextField()
	offer = models.BooleanField(default=False)
	price = models.IntegerField()