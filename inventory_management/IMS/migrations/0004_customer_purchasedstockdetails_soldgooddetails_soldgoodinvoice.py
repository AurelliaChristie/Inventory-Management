# Generated by Django 3.2.5 on 2021-07-16 04:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('IMS', '0003_product_productdetails'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CustomerName', models.CharField(max_length=255, null=True)),
                ('Telephone', models.CharField(blank=True, max_length=15, null=True)),
                ('EmailAddress', models.EmailField(blank=True, max_length=254, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SoldGoodInvoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SoldDate', models.DateField()),
                ('Customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='IMS.customer')),
            ],
        ),
        migrations.CreateModel(
            name='SoldGoodDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Size', models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('F', 'Free')], max_length=1, null=True)),
                ('Color', models.CharField(max_length=255, null=True)),
                ('Count', models.PositiveIntegerField(null=True)),
                ('Product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='IMS.product')),
                ('SInvoice', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='IMS.soldgoodinvoice')),
            ],
        ),
        migrations.CreateModel(
            name='PurchasedStockDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Size', models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('F', 'Free')], max_length=1, null=True)),
                ('Color', models.CharField(max_length=255, null=True)),
                ('Count', models.PositiveIntegerField(null=True)),
                ('PInvoice', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='IMS.purchasedstockinvoice')),
                ('Product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='IMS.product')),
            ],
        ),
    ]
