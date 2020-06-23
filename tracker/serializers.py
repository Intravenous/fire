from rest_framework import serializers
from .models import Stock, Trade, Wishlist, Investment, Portfolio, HistInvestmentValue

class StockSerializer(serializers.ModelSerializer):

    class Meta:
        model = Stock
        fields = ('symbol', 'company_name', 'primary_exchange', 'isin')

class TradeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Trade
        fields = ('__all__')

class WishlistSerializer(serializers.ModelSerializer):

    class Meta:
        model = Wishlist
        fields = ('user_id', 'stock_id', 'wishlist_name')

class InvestmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Investment
        fields = ('__all__')

class PortfolioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Portfolio
        fields = ('user_id', 'trade_id', 'investment_id')

class HistInvestmentValueSerializer(serializers.ModelSerializer):

    class Meta:
        model = HistInvestmentValue
        fields = ('investment_id', 'date', 'current_value')