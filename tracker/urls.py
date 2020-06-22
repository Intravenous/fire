from django.urls import path
from .views import StockListView, StockDetailView

urlpatterns = [
    path('', StockListView.as_view()),
    path('<int:pk>/', StockDetailView.as_view()),
]