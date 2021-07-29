from django.forms import ModelForm

from .models import *

# Purchase Form
class PurchaseForm(ModelForm):
    class Meta:
        model = PurchasedStockDetails
        fields = '__all__'

# Purchase Stock Invoice Register Form
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
