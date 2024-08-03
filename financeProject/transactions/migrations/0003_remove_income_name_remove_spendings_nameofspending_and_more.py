# Generated by Django 5.0.7 on 2024-08-03 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0002_rename_nameofincome_income_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='income',
            name='name',
        ),
        migrations.RemoveField(
            model_name='spendings',
            name='nameOfSpending',
        ),
        migrations.AddField(
            model_name='income',
            name='source',
            field=models.CharField(default='Unknown', max_length=15),
        ),
        migrations.AddField(
            model_name='income',
            name='title',
            field=models.CharField(default='Unknown', max_length=100),
        ),
        migrations.AddField(
            model_name='spendings',
            name='category',
            field=models.CharField(default='Unknown', max_length=15),
        ),
        migrations.AddField(
            model_name='spendings',
            name='title',
            field=models.CharField(default='Unknown', max_length=100),
        ),
        migrations.AlterField(
            model_name='income',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='spendings',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]