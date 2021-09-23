from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Dashboard view
    path('', views.dashboard, name='IMS-dashboard'),

    path('supplier_register/', views.supplier_register, name= 'IMS-supplier_register'),
    path('supplier_detail/<str:pk_supplier>/', views.supplier_detail, name= 'IMS-supplier_detail'),
    path('supplier_edit/<str:pk_supplier>/', views.supplier_edit, name= 'IMS-supplier_edit'),
    path('supplier_delete/<str:pk_supplier>/', views.supplier_delete, name= 'IMS-supplier_delete'),

    path('pinvoice_detail/<str:pk_pinvoice>/', views.pinvoice_detail, name= 'IMS-pinvoice_detail'),
    path('pinvoice_edit/<str:pk_pinvoice>/', views.pinvoice_edit, name= 'IMS-pinvoice_edit'),
    path('pinvoice_delete/<str:pk_pinvoice>/', views.pinvoice_delete, name= 'IMS-pinvoice_delete'),
    path('pinvoice_detail_edit/<str:pk_pinvoice_detail>/', views.pinvoice_detail_edit, name= 'IMS-pinvoice_detail_edit'),
    path('pinvoice_detail_delete/<str:pk_pinvoice_detail>/', views.pinvoice_detail_delete, name= 'IMS-pinvoice_detail_delete'),

    path('customer_register/', views.customer_register, name= 'IMS-customer_register'),
    path('customer_detail/<str:pk_customer>/', views.customer_detail, name= 'IMS-customer_detail'),
    path('customer_edit/<str:pk_customer>/', views.customer_edit, name= 'IMS-customer_edit'),
    path('customer_delete/<str:pk_customer>/', views.customer_delete, name='IMS-customer_delete'),

    path('product_category_register/', views.category_register, name= 'IMS-category_register'),
    path('product_register/', views.product_register, name= 'IMS-product_register'),
    path('product_detail/<str:pk_product>/', views.product_detail, name= 'IMS-product_detail'),

    path('purchase-stock/', views.purchase_stock, name= 'IMS-purchase_stock'),
    path('purchase-stock/register-invoice/', views.pinvoice_register, name= 'IMS-pinvoice_register'),
    
    path('sell-good/', views.sell_good, name= 'IMS-sell_good'),
    path('sell-good/register-invoice/', views.sinvoice_register, name= 'IMS-sinvoice_register'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)