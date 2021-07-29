from django.shortcuts import render, redirect

from .models import *
from .forms import *
from django.db.models import Count

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

# Purchase Stock
def purchase_stock(request):
    invoices = PurchasedStockInvoice.objects.all()
    detail_form = PurchaseForm()
    if request.method == 'POST':
        detail_form = PurchaseForm(request.POST)
        if detail_form.is_valid():
            detail_form.save()
            return redirect('/')
    context = {
        'detail_form' : detail_form,
        'invoices' : invoices
    }
    return render(request, 'IMS/purchase_stock.html', context)

# Purchase Stock Invoice Register
def pinvoice_register(request):
    invoice_form = PInvoiceForm()
    if request.method == 'POST':
        invoice_form = PInvoiceForm(request.POST)
        if invoice_form.is_valid():
            invoice_form.save()
            return redirect('IMS-purchase_stock')
    context = {
        'invoice_form': invoice_form
    }
    return render(request, 'IMS/pinvoice_register.html', context)

# Sell Good
def sell_good(request):
    invoices = SoldGoodInvoice.objects.all()
    detail_form = SellForm()
    if request.method == 'POST':
        detail_form = SellForm(request.POST)
        if detail_form.is_valid():
            detail_form.save()
            return redirect('/')
    context = {
        'detail_form' : detail_form,
        'invoices' : invoices
    }
    return render(request, 'IMS/sell_good.html', context)

# Sell Good Invoice Register
def sinvoice_register(request):
    invoice_form = SInvoiceForm()
    if request.method == 'POST':
        invoice_form = SInvoiceForm(request.POST)
        if invoice_form.is_valid():
            invoice_form.save()
            return redirect('IMS-sell_good')
    context = {
        'invoice_form': invoice_form
    }
    return render(request, 'IMS/sinvoice_register.html', context)
