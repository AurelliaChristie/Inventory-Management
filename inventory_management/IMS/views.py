from django.shortcuts import render

from .models import *

# Create your views here

# Dashboard
def dashboard(request):
    suppliers = Supplier.objects.all()
    context = {
        'suppliers' : suppliers
    }
    return render(request, 'IMS/dashboard.html', context)