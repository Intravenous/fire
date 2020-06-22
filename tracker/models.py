from django.db import models

# Create your models here.
class Stock(models.Model):
  symbol = models.CharField(max_length=4)
  companyName = models.CharField(max_length=50)
  primaryExchange = models.CharField(max_length=10)

  def __str__(self):
    return f'{self.symbol} - {self.companyName}'
  