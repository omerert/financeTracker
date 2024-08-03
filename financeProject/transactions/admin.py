from django.contrib import admin
from .models import Income, Spending, Transaction
# Register your models here.
admin.site.register(Income)
admin.site.register(Spending)
admin.site.register(Transaction)