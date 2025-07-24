from django.db import models

# Create your models here.
class homepage(models.Model):
    title = models.CharField(max_length=100, unique='True')
    description = models.CharField(max_length=200, null=False )     


class category(models.Model):  
    title = models.TextField(max_length=100)
    description=models.CharField(max_length=200, null=False) 
    
    def __str__(self):
        return self.title 