from django.db import models

# Create your models here.
class Income(models.Model):
    name = models.CharField(max_length=75)
    date = models.DateTimeField(auto_now_add=True)
    amount = models.FloatField()

    def __str__(self):
        return self.name
    
class Spendings(models.Model):
    nameOfSpending = models.CharField(max_length=75)
    date = models.DateTimeField(auto_now_add=True)
    amount = models.FloatField()