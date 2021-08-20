from django.forms import ModelForm

from .models import *

# Supplier Form
class SupplierForm(ModelForm):
    class Meta:
        model = Supplier
        fields = '__all__'

# Customer Form
class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

# Category Form
class CategoryForm(ModelForm):
    class Meta:
        model = ProductCategory
        fields = '__all__'

# Product Form
class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

# Purchase Form
class PurchaseForm(ModelForm):
    class Meta:
        model = PurchasedStockDetails
        fields = '__all__'

# Purchase Stock Invoice Form
class PInvoiceForm(ModelForm):
    class Meta:
        model = PurchasedStockInvoice
        fields = '__all__'

# Sell Form
class SellForm(ModelForm):
    class Meta:
        model = SoldGoodDetails
        fields = '__all__'

# Sell Good Invoice Register Form
class SInvoiceForm(ModelForm):
    class Meta:
        model = SoldGoodInvoice
        fields = '__all__'
