from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('top-millionaires/', views.top_millionaires, name='top_millionaires'),
    path('stocks/', views.stocks, name='stocks')
]
