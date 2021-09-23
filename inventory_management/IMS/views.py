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

    context = {
        'form' : form,
        'title' : 'Register Supplier'
    }
    return render(request, 'IMS/supplier_form.html', context)

## Supplier Detail
def supplier_detail(request, pk_supplier):
    supplier = Supplier.objects.get(id = pk_supplier)
    invoices = supplier.purchasedstockinvoice_set.all()
    context = {
        'supplier': supplier,
        'invoices': invoices,
        'title' : 'Supplier Detail'
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

    context = {
        'form': form,
        'title' : 'Edit Supplier'
    }
    return render(request, 'IMS/supplier_form.html', context)

## Supplier Delete
def supplier_delete(request, pk_supplier):
    supplier = Supplier.objects.get(id = pk_supplier)
    if request.method == 'POST':
        supplier.delete()
        return redirect('/')

    context = {
        'supplier' : supplier,
        'title' : 'Delete Supplier'
    }
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

    context = {
        'form': form,
        'title' : 'Register Customer'
    }
    return render(request, 'IMS/customer_form.html', context)

## Customer Detail
def customer_detail(request, pk_customer):
    customer = Customer.objects.get(id = pk_customer)
    invoices = customer.soldgoodinvoice_set.all()
    context = {
        'customer' : customer,
        'invoices' : invoices,
        'title' : 'Customer Detail'
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
    
    context = {
        'form' : form,
        'title' : 'Edit Customer'
    }
    return render(request, 'IMS/customer_form.html', context)

## Customer Delete
def customer_delete(request, pk_customer):
    customer = Customer.objects.get(id = pk_customer)
    if request.method == 'POST':
        customer.delete()
        return redirect('/')

    context = {
        'customer' : customer,
        'title' : 'Delete Customer'
    }
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
    
    context = {
        'form' : form,
        'title' : 'Register Category'
    }
    return render(request, 'IMS/category_form.html', context)


## Product Register
def product_register(request):
    form = ProductForm()

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    context = {
        'form' : form,
        'title' : 'Register Product'
    }
    return render(request, 'IMS/product_form.html', context)

## Product Detail
def product_detail(request, pk_product):
    product = Product.objects.get(id = pk_product)
    details = product.productdetails_set.all()
    context = {
        'product' : product,
        'details' : details,
        'title' : 'Product Detail'
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
        'invoices' : invoices,
        'title' : 'Purchase Stock'
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
        'form': form,
        'title' : 'Register Purchase Invoice'
    }
    return render(request, 'IMS/pinvoice_form.html', context)

# Purchase Stock Invoice Detail
def pinvoice_detail(request, pk_pinvoice):
    pinvoice = PurchasedStockInvoice.objects.get(id = pk_pinvoice)
    details = pinvoice.purchasedstockdetails_set.all()
    context = {
        'pinvoice' : pinvoice,
        'details' : details,
        'title' : 'Purchase Invoice Detail'
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
        
    context = {
        'form' : form,
        'title' : 'Edit Purchase Invoice'
    }
    return render(request, 'IMS/pinvoice_form.html', context)

# Purchase Stock Invoice Delete
def pinvoice_delete(request, pk_pinvoice):
    pinvoice = PurchasedStockInvoice.objects.get(id = pk_pinvoice)
    if request.method == 'POST':
        pinvoice.delete()
        return redirect('/')
    
    context = {
        'pinvoice': pinvoice,
        'title' : 'Delete Purchase Invoice'
    }
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
        'pinvoice_detail' : pinvoice_detail,
        'title' : 'Edit Purchase Detail'
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
        'pinvoice_detail' : pinvoice_detail,
        'title' : 'Delete Purchase Detail'
    }
    return render(request, 'IMS/pinvoice_detail_delete.html', context) 


# Sell Good
def sell_good(request):
    invoices = SoldGoodInvoice.objects.all()
    form = SellForm()
    if request.method == 'POST':
        form = SellForm(request.POST)
        if form.is_valid():
            sinvoice = form.cleaned_data.get('SInvoice')
            product = form.cleaned_data.get('Product')
            size = form.cleaned_data.get('Size')
            color = form.cleaned_data.get('Color')
            count = form.cleaned_data.get('Count')
            ProductDetails.objects.filter(Product = product, Size = size, Color = color).update(Count = F('Count')-count)

            form.save()
            return redirect('IMS-sinvoice_detail', pk_sinvoice=sinvoice.id)
    
    context = {
        'form' : form,
        'invoices' : invoices,
        'title' : 'Sell Good'
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
        'invoice_form': invoice_form,
        'title' : 'Register Sell Invoice'
    }
    return render(request, 'IMS/sinvoice_register.html', context)

# Sell Good Invoice Detail
def sinvoice_detail(request, pk_sinvoice):
    sinvoice = SoldGoodInvoice.objects.get(id = pk_sinvoice)
    details = sinvoice.soldgooddetails_set.all()
    context = {
        'sinvoice' : sinvoice,
        'details' : details,
        'title' : 'Sell Invoice Detail'
    }

    return render(request, 'IMS/sinvoice_detail.html', context)

# Sell Good Invoice Edit
def sinvoice_edit(request, pk_sinvoice):
    sinvoice = SoldGoodInvoice.objects.get(id = pk_sinvoice)
    form = SInvoiceForm(instance = sinvoice)

    if request.method == "POST":
        form = SInvoiceForm(request.POST, instance = sinvoice)
        if form.is_valid():
            form.save()
            return redirect('IMS-sinvoice_detail', pk_sinvoice=pk_sinvoice)
        
    context = {
        'form' : form,
        'title' : 'Edit Sell Invoice'
    }
    return render(request, 'IMS/sinvoice_form.html', context)

# Sell Good Invoice Delete
def sinvoice_delete(request, pk_sinvoice):
    sinvoice = SoldGoodInvoice.objects.get(id = pk_sinvoice)
    if request.method == 'POST':
        sinvoice.delete()
        return redirect('/')
    
    context = {
        'sinvoice': sinvoice,
        'title' : 'Delete Sell Invoice'
    }
    return render(request, 'IMS/sinvoice_delete.html', context) 

# Sell Good Invoice Detail Edit
def sinvoice_detail_edit(request, pk_sinvoice_detail):
    sinvoice_detail = SoldGoodDetails.objects.get(id = pk_sinvoice_detail)
    form = SellForm(instance = sinvoice_detail)
    old_count = sinvoice_detail.Count

    if request.method == "POST":
        form = SellForm(request.POST, instance = sinvoice_detail)
        if form.is_valid():
            sinvoice = form.cleaned_data.get('SInvoice')
            product = form.cleaned_data.get('Product')
            size = form.cleaned_data.get('Size')
            color = form.cleaned_data.get('Color')
            count = form.cleaned_data.get('Count')
            ProductDetails.objects.filter(Product = product, Size = size, Color = color).update(Count = F('Count')+old_count-count)
            form.save()
        return redirect('IMS-sinvoice_detail', pk_sinvoice = sinvoice.id)
    
    context = {
        'form' : form,
        'sinvoice_detail' : sinvoice_detail,
        'title' : 'Edit Sell Detail'
    }
    return render(request, 'IMS/sinvoice_detail_edit.html', context)

# Sell Good Invoice Detail Delete
def sinvoice_detail_delete(request, pk_sinvoice_detail):
    sinvoice_detail = SoldGoodDetails.objects.get(id = pk_sinvoice_detail)

    if request.method == 'POST':
        ProductDetails.objects.filter(Product = sinvoice_detail.Product, Size = sinvoice_detail.Size, Color = sinvoice_detail.Color).update(Count = F('Count')+sinvoice_detail.Count)
        sinvoice_detail.delete()
        return redirect('/')
    
    context = {
        'sinvoice_detail' : sinvoice_detail,
        'title' : 'Delete Sell Detail'
    }
    return render(request, 'IMS/sinvoice_detail_delete.html', context) 
