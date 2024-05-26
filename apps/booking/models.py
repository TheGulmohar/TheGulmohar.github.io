from enum import Enum
from django.db import models
from django.contrib.auth.models import User
from apps.gulmohar.models import Customer
from apps.utils.constants import CHOICES_ROOM_TYPE

class Room(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    capacity = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='rooms/')
    is_available = models.BooleanField(default=True)
    is_breakfast_included = models.BooleanField(default=False)
    room_type_quantity = models.IntegerField(default=0, blank=False)
    room_type = models.PositiveSmallIntegerField(choices=CHOICES_ROOM_TYPE, default=0)


    def __str__(self):
        return self.name

class Booking(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.customer.user.username} - {self.room.name} ({self.start_date} - {self.end_date})"