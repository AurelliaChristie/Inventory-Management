from django.shortcuts import render, redirect
from django.db.models import Count, F, Case, When

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
            return redirect('IMS-customer_detail')
    
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

# Product
## Category Register
def category_register(request):
    form = CategoryForm()

    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    context = {'form' : form}
    return render(request, 'IMS/category_form.html', context)


## Product Register
def product_register(request):
    form = ProductForm()

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    context = {'form' : form}
    return render(request, 'IMS/product_form.html', context)

## Product Detail
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
    form = PurchaseForm()
    if request.method == 'POST':
        form = PurchaseForm(request.POST)
        if form.is_valid():
            pinvoice = form.cleaned_data.get('PInvoice')
            product = form.cleaned_data.get('Product')
            size = form.cleaned_data.get('Size')
            color = form.cleaned_data.get('Color')
            count = form.cleaned_data.get('Count')
            if ProductDetails.objects.filter(Product = product, Size = size, Color = color).exists():
                ProductDetails.objects.filter(Product = product, Size = size, Color = color).update(Count = F('Count')+count)
            else:
                productdetails = ProductDetails(
                    Product = product,
                    Size = size,
                    Color = color,
                    Count = count
                )
                productdetails.save()

            form.save()
            return redirect('IMS-pinvoice_detail', pk_pinvoice=pinvoice.id)
    
    context = {
        'form' : form,
        'invoices' : invoices
    }
    return render(request, 'IMS/purchase_stock.html', context)

## Purchase Stock Invoice Register
def pinvoice_register(request):
    form = PInvoiceForm()
    if request.method == 'POST':
        form = PInvoiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('IMS-purchase_stock')
    context = {
        'form': form
    }
    return render(request, 'IMS/pinvoice_form.html', context)

# Purchase Stock Invoice Detail
def pinvoice_detail(request, pk_pinvoice):
    pinvoice = PurchasedStockInvoice.objects.get(id = pk_pinvoice)
    details = pinvoice.purchasedstockdetails_set.all()
    context = {
        'pinvoice' : pinvoice,
        'details' : details,
    }

    return render(request, 'IMS/pinvoice_detail.html', context)

# Purchase Stock Invoice Edit
def pinvoice_edit(request, pk_pinvoice):
    pinvoice = PurchasedStockInvoice.objects.get(id = pk_pinvoice)
    form = PInvoiceForm(instance = pinvoice)

    if request.method == "POST":
        form = PInvoiceForm(request.POST, instance = pinvoice)
        if form.is_valid():
            form.save()
            return redirect('IMS-pinvoice_detail', pk_pinvoice=pk_pinvoice)
        
    context = {'form' : form}
    return render(request, 'IMS/pinvoice_form.html', context)

# Purchase Stock Invoice Delete
def pinvoice_delete(request, pk_pinvoice):
    pinvoice = PurchasedStockInvoice.objects.get(id = pk_pinvoice)
    if request.method == 'POST':
        pinvoice.delete()
        return redirect('/')
    
    context = {'pinvoice': pinvoice}
    return render(request, 'IMS/pinvoice_delete.html', context) 

# Purchase Stock Invoice Detail Edit
def pinvoice_detail_edit(request, pk_pinvoice_detail):
    pinvoice_detail = PurchasedStockDetails.objects.get(id = pk_pinvoice_detail)
    form = PurchaseForm(instance = pinvoice_detail)
    old_count = pinvoice_detail.Count

    if request.method == "POST":
        form = PurchaseForm(request.POST, instance = pinvoice_detail)
        if form.is_valid():
            pinvoice = form.cleaned_data.get('PInvoice')
            product = form.cleaned_data.get('Product')
            size = form.cleaned_data.get('Size')
            color = form.cleaned_data.get('Color')
            count = form.cleaned_data.get('Count')
            ProductDetails.objects.filter(Product = product, Size = size, Color = color).update(Count = F('Count')-old_count+count)
            form.save()
        return redirect('IMS-pinvoice_detail', pk_pinvoice = pinvoice.id)
    
    context = {
        'form' : form,
        'pinvoice_detail' : pinvoice_detail
    }
    return render(request, 'IMS/pinvoice_detail_edit.html', context)

# Purchase Stock Invoice Detail Delete
def pinvoice_detail_delete(request, pk_pinvoice_detail):
    pinvoice_detail = PurchasedStockDetails.objects.get(id = pk_pinvoice_detail)

    if request.method == 'POST':
        ProductDetails.objects.filter(Product = pinvoice_detail.Product, Size = pinvoice_detail.Size, Color = pinvoice_detail.Color).update(Count = F('Count')-pinvoice_detail.Count)
        pinvoice_detail.delete()
        return redirect('/')
    
    context = {
        'pinvoice_detail' : pinvoice_detail
    }
    return render(request, 'IMS/pinvoice_detail_delete.html', context) 


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

# Sell Good Invoice Detail

# Sell Good Invoice Delete