from django.db import models
from django.db.models.fields import CharField, DateField, EmailField, PositiveIntegerField, TextField, URLField
from django.db.models.fields.files import ImageField
from django.db.models.fields.related import ForeignKey
from django.contrib.auth.models import User

# Product Category
class ProductCategory(models.Model):
    ProductCategory =  CharField(max_length = 255, null=True)
    User = ForeignKey(User, null=True, on_delete = models.CASCADE)

    def __str__(self):
        return self.ProductCategory

# Product
class Product(models.Model):
    ProductName = CharField(max_length = 255, null=True)
    ProductCategory = ForeignKey(ProductCategory, null=True, on_delete = models.SET_NULL)
    ProductDescription = TextField(null=True, blank=True)
    ProductImage = ImageField(upload_to = "ProductImage/", null=True, blank = True)
    User = ForeignKey(User, null=True, on_delete = models.CASCADE)

    def __str__(self):
        return str(self.ProductCategory) + "_" + str(self.ProductName)

# Product Details
class ProductDetails(models.Model):
    # Foreign Key
    Product = ForeignKey(Product, null=True, on_delete = models.CASCADE)

    PRODUCT_SIZE = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('F', 'Free')
    )

    Size = CharField(max_length = 1, null=True, choices = PRODUCT_SIZE)
    Color = CharField(max_length = 255, null=True)
    Count = PositiveIntegerField(null=True)
    User = ForeignKey(User, null=True, on_delete = models.CASCADE)

    def __str__(self):
        return str(self.Product) + "_" + str(self.Size) + "_" + str(self.Color)

# Purchase Product
## Supplier
class Supplier(models.Model):
    SupplierName = CharField(max_length = 255, null=True)
    OnlineShopURL = URLField(null=True)
    Telephone = CharField(max_length = 15, null=True, blank=True)
    EmailAddress = EmailField(null=True, blank=True)
    JoinDate = DateField(null=True, auto_now_add=True)
    User = ForeignKey(User, null=True, on_delete = models.CASCADE)

    def __str__(self):
        return self.SupplierName

## Purchased Stock Invoice
class PurchasedStockInvoice(models.Model):
    # Foreign Key
    Supplier = models.ForeignKey(Supplier, null=True, on_delete = models.SET_NULL)
    User = ForeignKey(User, null=True, on_delete = models.CASCADE)

    PurchaseDate = DateField()

    def __str__(self):
        return str(self.Supplier) + "_" + str(self.PurchaseDate)
    
## Purchased Stock Details
class PurchasedStockDetails(models.Model):
    # Foreign Key
    PInvoice = ForeignKey(PurchasedStockInvoice, null=True, on_delete = models.CASCADE)
    Product = ForeignKey(Product, null=True, on_delete=models.CASCADE)
    User = ForeignKey(User, null=True, on_delete = models.CASCADE)

    PRODUCT_SIZE = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('F', 'Free')
    )
    Size = CharField(max_length = 1, null=True, choices = PRODUCT_SIZE)
    Color = CharField(max_length = 255, null=True)
    Count = PositiveIntegerField(null=True)

    def __str__(self):
        return str(self.PInvoice)+"_" + str(self.Product) + "_" + str(self.Size) + "_" + str(self.Color)

# Sell Product
## Customer
class Customer(models.Model):
    CustomerName = CharField(max_length = 255, null=True)
    Telephone = CharField(max_length = 15, null=True, blank=True)
    EmailAddress = EmailField(null=True, blank=True)
    JoinDate = DateField(null=True, auto_now_add=True)
    User = ForeignKey(User, null=True, on_delete = models.CASCADE)

    def __str__(self):
        return self.CustomerName

## Sold Good Invoice
class SoldGoodInvoice(models.Model):
    # Foreign Key
    Customer = models.ForeignKey(Customer, null=True, on_delete = models.SET_NULL)
    User = ForeignKey(User, null=True, on_delete = models.CASCADE)
    
    SoldDate = DateField()

    def __str__(self):
        return str(self.Customer) + "_" + str(self.SoldDate)
    
## Sold Good Details
class SoldGoodDetails(models.Model):
    # Foreign Key
    SInvoice = ForeignKey(SoldGoodInvoice, null=True, on_delete = models.CASCADE)
    Product = ForeignKey(Product, null=True, on_delete=models.CASCADE)
    User = ForeignKey(User, null=True, on_delete = models.CASCADE)

    PRODUCT_SIZE = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('F', 'Free')
    )
    Size = CharField(max_length = 1, null=True, choices = PRODUCT_SIZE)
    Color = CharField(max_length = 255, null=True)
    Count = PositiveIntegerField(null=True)

    def __str__(self):
        return str(self.SInvoice)+"_" + str(self.Product) + "_" + str(self.Size) + "_" + str(self.Color)
