from rest_framework.views import APIView # get the APIView class from DRF
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from rest_framework.response import Response # get the Response class from DRF

from .models import Stock, Trade, Wishlist, Investment, Portfolio, HistInvestmentValue
from .serializers import StockSerializer, TradeSerializer, WishlistSerializer, InvestmentSerializer, PortfolioSerializer, HistInvestmentValueSerializer

# Create your views here.
# class StockListView(APIView): # extend the APIView

#     def get(self, _request):
#         stocks = Stock.objects.all()
#         serializer = StockSerializer(stocks, many=True)

#         return Response(serializer.data) # send the JSON to the client


# class StockDetailView(APIView): # extend the APIView

#     def get(self, _request, pk):
#         stock = Stock.objects.get(pk=pk) # get a book by id (pk means primary key)
#         serializer = StockSerializer(stock)

#         return Response(serializer.data) # send the JSON to the client

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


class WishlistListView(ListCreateAPIView):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer

class WishlistDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer


class InvestmentListView(ListCreateAPIView):
    queryset = Investment.objects.all()
    serializer_class = InvestmentSerializer

class InvestmentDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Investment.objects.all()
    serializer_class = InvestmentSerializer


class PortfolioListView(ListCreateAPIView):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer

class PortfolioDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer


class HistInvestmentValueListView(ListCreateAPIView):
    queryset = HistInvestmentValue.objects.all()
    serializer_class = HistInvestmentValueSerializer

class HistInvestmentValueDetailView(RetrieveUpdateDestroyAPIView):
    queryset = HistInvestmentValue.objects.all()
    serializer_class = HistInvestmentValueSerializer