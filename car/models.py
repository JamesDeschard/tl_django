from django.db import models
from django.shortcuts import reverse

## Cars ##

class AuctionHouse(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.name

class Locale(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.name
    
class Manufacturer(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.name

class Vehicle(models.Model):
    car = models.CharField(max_length=100)
    car_name = models.CharField(max_length=100)
    image = models.URLField()
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    model_year = models.IntegerField()
    serial_number = models.CharField(max_length=100)
    date_auctioned = models.DateField()
    auction_house = models.ForeignKey(AuctionHouse, on_delete=models.CASCADE)
    locale = models.ForeignKey(Locale, on_delete=models.CASCADE)
    original_price = models.IntegerField()
    adjusted_price = models.IntegerField()
    wikipedia_profile = models.URLField()
    description = models.TextField()
    
    def __str__(self) -> str:
        return self.car_name


    