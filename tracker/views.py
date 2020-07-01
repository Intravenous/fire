from rest_framework.views import APIView # get the APIView class from DRF
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response # get the Response class from DRF
# Import different permisson classes
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

# Extend Django's permissions
from rest_framework.permissions import BasePermission

from .models import Stock, Trade, Wishlist, Investment, Portfolio, HistInvestmentValue
from .serializers import StockSerializer, TradeSerializer, WishlistSerializer, InvestmentSerializer, PortfolioSerializer, HistInvestmentValueSerializer, PopulatedWishlistSerializer, PopulatedPortfolioSerializer

# class IsOwnerOrReadOnly(BasePermission):
#     def has_object_permission(self, _request, view, obj):

# Create your views here.
class StockListView(ListCreateAPIView):
  queryset = Stock.objects.all()
  serializer_class = StockSerializer
  permmission_classes = (IsAuthenticated,)

class StockDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer


class TradeListView(ListCreateAPIView):
    queryset = Trade.objects.all()
    serializer_class = TradeSerializer

class TradeDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Trade.objects.all()
    serializer_class = TradeSerializer

# Doesn't populate symbol for some reason, need to investigate if required
# Reason could be because i haven't overrided the generic views with the populated serializer
# class TradeListView(ListCreateAPIView):
#     queryset = Trade.objects.all()
#     serializer_class = PopulatedTradeSerializer

# class TradeDetailView(RetrieveUpdateDestroyAPIView):
#     queryset = Trade.objects.all()
#     serializer_class = PopulatedTradeSerializer

# class UserListView(ListCreateAPIView):
#   queryset= User.objects.all()
#   serializer_class = UserSerializer


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

    # def get(self, _request):
    #     portfolios = Portfolio.objects.all()
    #     serializer = PopulatedPortfolioSerializer(portfolios, many=True)

    #     return Response(serializer.data)

class PortfolioDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Portfolio.objects.all()
    serializer_class = PopulatedPortfolioSerializer
    permission_classes = (IsAuthenticated,)

    # def get(self, _request, pk):
    #     portfolio = Portfolio.objects.get(pk=pk)
    #     serializer = PopulatedPortfolioSerializer(portfolio)

    #     return Response(serializer.data)

class HistInvestmentValueListView(ListCreateAPIView):
    queryset = HistInvestmentValue.objects.all()
    serializer_class = HistInvestmentValueSerializer

class HistInvestmentValueDetailView(RetrieveUpdateDestroyAPIView):
    queryset = HistInvestmentValue.objects.all()
    serializer_class = HistInvestmentValueSerializer