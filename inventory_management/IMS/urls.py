from django.urls import path
from . import views

urlpatterns = [
    # Dashboard view
    path('', views.dashboard, name='IMS-dashboard'),
    path('purchase-stock/', views.purchase_stock, name='IMS-purchase_stock'),
    path('purchase-stock/register-invoice/', views.pinvoice_register, name='IMS-pinvoice_register'),
    path('sell-good/', views.sell_good, name='IMS-sell_good'),
    path('sell-good/register-invoice/', views.sinvoice_register, name='IMS-sinvoice_register'),
]