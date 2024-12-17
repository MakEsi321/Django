from django.shortcuts import render
from .models import Millionaire
from .models import Stock


def index(request):
    data = {
        'title': 'Виртуальный миллионер',
    }
    return render(request, 'main/index.html', data)


def about(request):
    return render(request, 'main/about.html')


def top_millionaires(request):
    millionaires = Millionaire.objects.all().order_by('-net_worth')
    return render(request, 'main/top_millionaires.html', {'millionaires': millionaires})


def stocks(request):
    stocks = Stock.objects.all()  # Получаем все акции из базы данных
    return render(request, 'main/stocks.html', {'stocks': stocks})