from django.forms import ModelForm

from .models import *

# Supplier Form
class SupplierForm(ModelForm):
    class Meta:
        model = Supplier
        exclude = ('User',)

# Customer Form
class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        exclude = ('User',)

# Category Form
class CategoryForm(ModelForm):
    class Meta:
        model = ProductCategory
        exclude = ('User',)

# Product Form
class ProductForm(ModelForm):
    class Meta:
        model = Product
        exclude = ('User',)

# Purchase Form
class PurchaseForm(ModelForm):
    class Meta:
        model = PurchasedStockDetails
        exclude = ('User',)

# Purchase Stock Invoice Form
class PInvoiceForm(ModelForm):
    class Meta:
        model = PurchasedStockInvoice
        exclude = ('User',)

# Sell Form
class SellForm(ModelForm):
    class Meta:
        model = SoldGoodDetails
        exclude = ('User',)

# Sell Good Invoice Register Form
class SInvoiceForm(ModelForm):
    class Meta:
        model = SoldGoodInvoice
        exclude = ('User',)
