from django.db import models


class Millionaire(models.Model):
    name = models.CharField(max_length=100)
    net_worth = models.DecimalField(max_digits=15, decimal_places=2)
    country = models.CharField(max_length=100)
    industry = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Stock(models.Model):
    symbol = models.CharField(max_length=10)  # Символ акции, например: 'AAPL' для Apple
    company_name = models.CharField(max_length=100)  # Название компании
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Цена акции
    change_percentage = models.DecimalField(max_digits=5, decimal_places=2)  # Процентное изменение цены

    def __str__(self):
        return f'{self.company_name} ({self.symbol})'
