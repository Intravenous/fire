from rest_framework import serializers

from .models import Stock, Trade, Wishlist, Investment, Portfolio, HistInvestmentValue

class StockSerializer(serializers.ModelSerializer):

    class Meta:
        model = Stock
        fields = ('id', 'symbol', 'company_name', 'primary_exchange', 'isin')

class TradeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Trade
        fields = ('id', 'user_id', 'symbol', 'date_bought', 'number_of_shares', 'price_per_share', 'commission', 'stamp_duty', 'total_cost', 'account_type', 'broker', 'comment', 'sold')

# Doesn't populate symbol for some reason, need to investigate if required
# class PopulatedTradeSerializer(serializers.ModelSerializer):

#   symbol = StockSerializer

#   class Meta:
#       model = Trade
#       fields = ('id', 'user_id', 'symbol', 'date_bought', 'number_of_shares', 'price_per_share', 'commission', 'stamp_duty', 'total_cost', 'account_type', 'broker', 'comment', 'sold')

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
        fields = ('id', 'investment_id', 'date', 'current_value')


class PopulatedWishlistSerializer(serializers.ModelSerializer):

  stock_id = StockSerializer(many=True)

  class Meta:
    model = Wishlist
    fields = ('user_id', 'stock_id', 'wishlist_name')

class PopulatedPortfolioSerializer(serializers.ModelSerializer):

  trade_id = TradeSerializer(many=True)
  investment_id = InvestmentSerializer(many=True)

  class Meta:
      model = Portfolio
      fields = ('user_id', 'trade_id', 'investment_id')