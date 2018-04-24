from django.db import models

# Create your models here.
class Order(models.Model):
	item = models.CharField(max_length=180, null= True, blank=True)
	address = models.CharField(max_length=180, null=True, blank=True)