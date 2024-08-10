from django.shortcuts import render
from .models import Transaction
from django.db.models import Sum
# Create your views here.


def listTransaction(request):
    transactions = Transaction.objects.all().order_by("-date")
    expences = Transaction.objects.filter(transactionType='E')
    totalExpence = sum(t.amount for t in expences)
     # Calculate percentage for each transaction
    for t in transactions:
        t.percentage = (t.amount / totalExpence) * 100
    return render(request, 'transactions.html', {'transactions': transactions, 'totalExpense': totalExpence})

