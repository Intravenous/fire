from django.db import models

# Module added that auto creates a child model on creation of a parent module
# Added to auto create a portfolio on creation of a user
from django_auto_one_to_one import AutoOneToOneModel

from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
class Stock(models.Model):
  symbol = models.CharField(max_length=4)
  company_name = models.CharField(max_length=50)
  primary_exchange = models.CharField(max_length=10)
  isin = models.CharField(max_length=12)

  def __str__(self):
    return f'{self.symbol} - {self.company_name}'

class Trade(models.Model):
  user_id = models.ForeignKey(
        User, related_name='trade', on_delete=models.CASCADE)
  symbol = models.ForeignKey(
        Stock, related_name='trade', on_delete=models.CASCADE)
  date_bought = models.DateField()
  number_of_shares = models.DecimalField(max_digits=10, decimal_places=5)
  price_per_share = models.DecimalField(max_digits=10, decimal_places=5)
  commission = models.DecimalField(max_digits=4, decimal_places=2)
  stamp_duty = models.DecimalField(max_digits=10, decimal_places=2)
  total_cost = models.DecimalField(max_digits=10, decimal_places=2)
  account_type = models.CharField(max_length=20)
  broker = models.CharField(max_length=50)
  comment = models.CharField(blank=True, max_length=50)
  sold = models.BooleanField()

  def __str__(self):
    return f'{self.user_id} - {self.symbol}'

class Investment(models.Model):
  user_id = models.ForeignKey(
        User, related_name='investment', on_delete=models.CASCADE)
  investment_date = models.DateField()
  CASH = 'CH'
  CASH_ISA = 'CI'
  EQUITY_CROWDFUNDING = 'EC'
  PENSION = 'PN'
  INVESTMENT_TYPE_CHOICES = [
    (CASH, 'Cash'),
    (CASH_ISA, 'Cash ISA'),
    (EQUITY_CROWDFUNDING, 'Equity Crowdfunding'),
    (PENSION, 'Pension'),
  ]
  investment_type = models.CharField(
    max_length=2,
    choices=INVESTMENT_TYPE_CHOICES,
    default=CASH,
    )
  investment_name = models.CharField(max_length=50)
  initial_value = models.DecimalField(max_digits=10, decimal_places=5)
  comment = models.CharField(blank=True, max_length=50)
  sold = models.BooleanField(default=False)
  
  
  def __str__(self):
    return f'{self.user_id} - {self.investment_type} - {self.investment_name}'

class HistInvestmentValue(models.Model):
  investment_id = models.ForeignKey(
        Investment, related_name='histInvestmentValue', on_delete=models.CASCADE)
  date = models.DateField()
  current_value = models.DecimalField(max_digits=10, decimal_places=5)

  def __str__(self):
    return f'{self.investment_id}'

class Wishlist(models.Model):
  user_id = models.ForeignKey(
        User, related_name='wishlist', on_delete=models.CASCADE)
  stock_id = models.ManyToManyField(Stock, related_name='wishlist')
  wishlist_name = models.CharField(max_length=100)

  def __str__(self):
    return f'{self.user_id} - {self.wishlist_name}'

class Portfolio(AutoOneToOneModel(User)):
# User_id & Portfolio auto added when user created
  trade_id = models.ManyToManyField(Trade, related_name='portfolio', blank=True)
  investment_id = models.ManyToManyField(Investment, related_name='portfolio', blank=True)
