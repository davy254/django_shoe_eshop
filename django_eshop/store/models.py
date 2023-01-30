import uuid
from django.db import models
from django.contrib.auth.models import User
from sqlalchemy import true


# Customer model
class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name

# Product model
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()

    def __str__(self) -> str:
        return self.name

# Order model
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.UUIDField(default=uuid.uuid4, editable=False)

    def __str__(self) -> str:
        return str(self.id)

# OrderItem model
class OrderItem(models.Model):
    product =  models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)