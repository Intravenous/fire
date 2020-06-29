from rest_framework.views import APIView # get the APIView class from DRF
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from rest_framework.response import Response # get the Response class from DRF

from .models import Stock, Trade, Wishlist, Investment, Portfolio, HistInvestmentValue
from .serializers import StockSerializer, TradeSerializer, WishlistSerializer, InvestmentSerializer, PortfolioSerializer, HistInvestmentValueSerializer, PopulatedWishlistSerializer, PopulatedPortfolioSerializer

# Create your views here.
class StockListView(ListCreateAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

class StockDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer


class TradeListView(ListCreateAPIView):
    queryset = Trade.objects.all()
    serializer_class = TradeSerializer

class TradeDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Trade.objects.all()
    serializer_class = TradeSerializer

# Doesn't populated symbol for some reason, need to investigate if required
# class TradeListView(ListCreateAPIView):
#     queryset = Trade.objects.all()
#     serializer_class = PopulatedTradeSerializer

# class TradeDetailView(RetrieveUpdateDestroyAPIView):
#     queryset = Trade.objects.all()
#     serializer_class = PopulatedTradeSerializer


class WishlistListView(ListCreateAPIView):
    queryset = Wishlist.objects.all()
    serializer_class = PopulatedWishlistSerializer

class WishlistDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Wishlist.objects.all()
    serializer_class = PopulatedWishlistSerializer


class InvestmentListView(ListCreateAPIView):
    queryset = Investment.objects.all()
    serializer_class = InvestmentSerializer

class InvestmentDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Investment.objects.all()
    serializer_class = InvestmentSerializer


class PortfolioListView(ListCreateAPIView):
    queryset = Portfolio.objects.all()
    serializer_class = PopulatedPortfolioSerializer

class PortfolioDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Portfolio.objects.all()
    serializer_class = PopulatedPortfolioSerializer


class HistInvestmentValueListView(ListCreateAPIView):
    queryset = HistInvestmentValue.objects.all()
    serializer_class = HistInvestmentValueSerializer

class HistInvestmentValueDetailView(RetrieveUpdateDestroyAPIView):
    queryset = HistInvestmentValue.objects.all()
    serializer_class = HistInvestmentValueSerializer