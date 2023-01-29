from django.shortcuts import render
from matplotlib.style import context

# Store view
def store(request):
    context = {}
    return render(request, 'store/store.html', context)

# Cart view
def cart(request):
    context = {}
    return render(request, 'store/cart.html', context)

# Check-out view
def checkout(request):
    context = {}
    return render(request, 'store/checkout.html', context)
