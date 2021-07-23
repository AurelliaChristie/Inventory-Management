from django.shortcuts import render

from .models import *
from django.db.models import Count
# Create your views here

# Dashboard
def dashboard(request):
    suppliers = Supplier.objects.all()
    customers = Customer.objects.all()
    products = Product.objects.all()
    categories = ProductCategory.objects.all().annotate(product_count = Count('product'))
    context = {
        'suppliers' : suppliers,
        'customers' : customers,
        'products' : products,
        'categories' : categories
    }
    return render(request, 'IMS/dashboard.html', context)