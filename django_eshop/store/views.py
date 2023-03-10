from django.shortcuts import render
from .models import Product


# Store view
def store(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request, 'store/store.html', context)

# Cart view
def cart(request):
    context = {}
    return render(request, 'store/cart.html', context)

# Check-out view
def checkout(request):
    context = {}
    return render(request, 'store/checkout.html', context)
