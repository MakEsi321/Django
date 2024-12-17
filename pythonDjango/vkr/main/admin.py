from django.contrib import admin
from .models import Millionaire
from .models import Stock

admin.site.register(Millionaire)
admin.site.register(Stock)
