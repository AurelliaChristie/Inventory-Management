from django.contrib import admin

# Import models
from .models import *

# Register models
admin.site.register(ProductCategory)
admin.site.register(Product)
admin.site.register(ProductDetails)
admin.site.register(Supplier)
admin.site.register(PurchasedStockInvoice)
admin.site.register(PurchasedStockDetails)
admin.site.register(Customer)
admin.site.register(SoldGoodInvoice)
admin.site.register(SoldGoodDetails)