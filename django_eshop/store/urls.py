from django.urls import path
from .views import cart, checkout, store

urlpatterns = [
    path('', store, name='store'),
    path('cart/', cart, name='cart'),
    path('checkout/', checkout, name='checkout')
]