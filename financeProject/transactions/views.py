from django.shortcuts import render
from .models import Income, Spending, Transaction
from django.db.models import Sum
# Create your views here.

def listIncome(request):
    incomes = Income.objects.all().order_by("-date")
    return render(request, 'income/income.html', {'incomes': incomes})
def listTransaction(request):
    transactions = Transaction.objects.all().order_by("-date")
    totalExpense = Transaction.objects.filter(transactionType='E')
    total_expense_amount = totalExpense.aggregate(Sum('amount'))['amount__sum']
    return render(request, 'transactions.html', {'transactions': transactions, 'totalExpense': total_expense_amount})

