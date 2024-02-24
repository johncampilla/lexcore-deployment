# Generated by Django 4.2.6 on 2024-01-17 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0003_invoiceimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='bills',
            name='hourlyrate',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='bills',
            name='lawyer_name',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
    ]