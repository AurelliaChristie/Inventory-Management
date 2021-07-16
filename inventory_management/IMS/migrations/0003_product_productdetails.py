# Generated by Django 3.2.5 on 2021-07-16 04:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('IMS', '0002_auto_20210716_1047'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ProductName', models.CharField(max_length=255, null=True)),
                ('ProductCategory', models.CharField(max_length=255, null=True)),
                ('ProductDescription', models.TextField(blank=True, null=True)),
                ('ProductImage', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='ProductDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Size', models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('F', 'Free')], max_length=1, null=True)),
                ('Color', models.CharField(max_length=255, null=True)),
                ('Count', models.PositiveIntegerField(null=True)),
                ('Product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='IMS.product')),
            ],
        ),
    ]
