from django.urls import path
from .views import StockListView, StockDetailView, TradeListView, TradeDetailView, WishlistListView, WishlistDetailView, InvestmentListView, InvestmentDetailView, PortfolioListView, PortfolioDetailView, HistInvestmentValueListView, HistInvestmentValueDetailView

urlpatterns = [
    path('stock/', StockListView.as_view()),
    path('stock/<int:pk>/', StockDetailView.as_view()),
    path('trade/', TradeListView.as_view()),
    path('trade/<int:pk>/', TradeDetailView.as_view()),
    path('wishlist/', WishlistListView.as_view()),
    path('wishlist/<int:pk>/', WishlistDetailView.as_view()),
    path('investment/', InvestmentListView.as_view()),
    path('investment/<int:pk>/', InvestmentDetailView.as_view()),
    path('portfolio/', PortfolioListView.as_view()),
    path('portfolio/<int:pk>/', PortfolioDetailView.as_view()),
    path('histvalue/', HistInvestmentValueListView.as_view()),
    path('histvalue/<int:pk>/', HistInvestmentValueDetailView.as_view()),
]
