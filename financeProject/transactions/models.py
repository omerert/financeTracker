from django.db import models

# Create your models here.
class Income(models.Model):
    title = models.CharField(max_length=100, default='Unknown')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    source = models.CharField(max_length=15, default='Unknown')

    
class Spending(models.Model):
    title = models.CharField(max_length=100, default='Unknown')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=15, default='Unknown')
    
class Transaction(models.Model):
    TRANSACTION_TYPE = {
        "I": "Income",
        "E": "Expense",
    }
    EXPENCE_TYPE  = {
    'food': 'Food',
    'transportation': 'Transportation',
    'housing': 'Housing',
    'utilities': 'Utilities',
    'entertainment': 'Entertainment',
    'healthcare': 'Healthcare',
    'education': 'Education',
    'clothing': 'Clothing',
    'insurance': 'Insurance',
    'savings': 'Savings',
    'miscellaneous': 'Miscellaneous'
    }
    title = models.CharField(max_length=20)
    transactionType = models.CharField(max_length=1,choices=TRANSACTION_TYPE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField()
    expenceType = models.CharField(max_length=15, choices=EXPENCE_TYPE)