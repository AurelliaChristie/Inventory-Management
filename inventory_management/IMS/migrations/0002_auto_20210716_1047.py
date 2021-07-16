# Generated by Django 3.2.5 on 2021-07-16 03:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('IMS', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplier',
            name='EmailAddress',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='OnlineShopURL',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='SupplierName',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='Telephone',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.CreateModel(
            name='PurchasedStockInvoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PurchaseDate', models.DateField()),
                ('Supplier', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='IMS.supplier')),
            ],
        ),
    ]