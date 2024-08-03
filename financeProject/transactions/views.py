from django.shortcuts import render
from .models import Income, Spendings
# Create your views here.

def listIncome(request):
    incomes = Income.objects.all().order_by("-date")
    return render(request, 'income.html', {'incomes': incomes})