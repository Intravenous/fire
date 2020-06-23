from django.contrib import admin
from .models import Stock, Trade, Wishlist, Investment, Portfolio, HistInvestmentValue

# Register your models here.
admin.site.register(Stock)
admin.site.register(Trade)
admin.site.register(Wishlist)
admin.site.register(Investment)
admin.site.register(Portfolio)
admin.site.register(HistInvestmentValue)
