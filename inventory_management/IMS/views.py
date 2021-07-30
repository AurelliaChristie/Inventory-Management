from django.shortcuts import render, redirect
from django.db.models import Count

from .models import *
from .forms import *


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

# Supplier
## Supplier Register
def supplier_register(request):
    form = SupplierForm()

    if request.method == "POST":
        form = SupplierForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form' : form}
    return render(request, 'IMS/supplier_form.html', context)

## Supplier Detail
def supplier_detail(request, pk_supplier):
    supplier = Supplier.objects.get(id = pk_supplier)
    invoices = supplier.purchasedstockinvoice_set.all()
    context = {
        'supplier': supplier,
        'invoices': invoices,
    }
    return render(request, 'IMS/supplier_detail.html', context)

## Supplier Edit
def supplier_edit(request, pk_supplier):
    supplier = Supplier.objects.get(id=pk_supplier)
    form = SupplierForm(instance=supplier)

    if request.method == 'POST':
        form = SupplierForm(request.POST, instance=supplier)
        if form.is_valid():
            form.save()
            return redirect('/') 

    context = {'form': form}
    return render(request, 'IMS/supplier_form.html', context)

## Supplier Delete
def supplier_delete(request, pk_supplier):
    supplier = Supplier.objects.get(id = pk_supplier)
    if request.method == 'POST':
        supplier.delete()
        return redirect('/')

    context = {'supplier' : supplier}
    return render(request, 'IMS/supplier_delete.html', context)

# Customer
## Customer Register
def customer_register(request):
    form = CustomerForm()

    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'IMS/customer_form.html', context)

## Customer Detail
def customer_detail(request, pk_customer):
    customer = Customer.objects.get(id = pk_customer)
    invoices = customer.soldgoodinvoice_set.all()
    context = {
        'customer' : customer,
        'invoices' : invoices
    }
    return render(request, 'IMS/customer_detail.html', context)

## Customer Edit
def customer_edit(request, pk_customer):
    customer = Customer.objects.get(id = pk_customer)
    form = CustomerForm(instance = customer)

    if request.method == "POST":
        form = CustomerForm(request.POST, instance = customer)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    context = {'form' : form}
    return render(request, 'IMS/customer_form.html', context)

## Customer Delete
def customer_delete(request, pk_customer):
    customer = Customer.objects.get(id = pk_customer)
    if request.method == 'POST':
        customer.delete()
        return redirect('/')

    context = {'customer' : customer}
    return render(request, 'IMS/customer_delete.html', context)


# Product Detail
def product_detail(request, pk_product):
    product = Product.objects.get(id = pk_product)
    details = product.productdetails_set.all()
    context = {
        'product' : product,
        'details' : details,
    }

    return render(request, 'IMS/product_detail.html', context)


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
