from django.db import models

# Create your models here.
from django.db import models


class Customer(models.Model):
    CustomerName = models.CharField(max_length=200, primary_key=True)

    def __str__(self):
        return self.CustomerName


class SaleDeed(models.Model):
    Customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    DocNo = models.CharField(max_length=200)
    ExecutedBy = models.CharField(max_length=200)
    FavourOf = models.CharField(max_length=200)
    LaterDate = models.DateField()
    SaidName = models.CharField(max_length=200)
    Property = models.CharField(max_length=200)
    To = models.CharField(max_length=200)
    BeforeSRO = models.CharField(max_length=200)

class SettlementDeed(models.Model):
    Customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    LaterDate = models.DateField()
    SaidName = models.CharField(max_length=200)
    ExecutedBy = models.CharField(max_length=200)
    Relation = models.CharField(max_length=100)
    Property = models.CharField(max_length=200)
    DocNo = models.CharField(max_length=200)
    BeforeSRO = models.CharField(max_length=200)

    def __str__(self):
        return self.Customer.CustomerName
