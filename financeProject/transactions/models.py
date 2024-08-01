from django.db import models

# Create your models here.
class Income(models.model):
    nameOfIncome = models.CharField(max_length=75)
    date = models.DateTimeField(auto_now_add=True)
    amount = models.FloatField()
class Spendings(models.model):
    nameOfSpending = models.CharField(max_length=75)
    date = models.DateTimeField(auto_now_add=True)
    amount = models.FloatField()