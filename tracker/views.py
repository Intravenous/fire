from rest_framework.views import APIView # get the APIView class from DRF
from rest_framework.response import Response # get the Response class from DRF

from .models import Stock
from .serializers import StockSerializer

# Create your views here.
class StockListView(APIView): # extend the APIView

    def get(self, _request):
        stocks = Stock.objects.all()
        serializer = StockSerializer(stocks, many=True)

        return Response(serializer.data) # send the JSON to the client


class StockDetailView(APIView): # extend the APIView

    def get(self, _request, pk):
        stock = Stock.objects.get(pk=pk) # get a book by id (pk means primary key)
        serializer = StockSerializer(stock)

        return Response(serializer.data) # send the JSON to the client
