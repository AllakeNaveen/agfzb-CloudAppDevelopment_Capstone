from django.db import models
from django.utils.timezone import now

class CarMake(models.Model):
    """
    Model to save data about a car make.
    """
    name = models.CharField(max_length=100)
    description = models.TextField()
    # Add any other fields you want for a car make

    def __str__(self):
        return self.name

class CarModel(models.Model):
    """
    Model to save data about a car model.
    """
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    dealer_id = models.IntegerField()  # Assuming you have a Dealer model or field in the Cloudant database
    name = models.CharField(max_length=100)
    
    TYPE_CHOICES = [
        ('Sedan', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
    ]
    type = models.CharField(max_length=5, choices=TYPE_CHOICES)
    year = models.DateField()
    # Add any other fields you want for a car model

    def __str__(self):
        return f"{self.car_make} - {self.name}"
