# Generated by Django 4.2.6 on 2024-02-08 21:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('emailportal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='emails',
            name='sentby',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='emails',
            name='message',
            field=models.TextField(blank=True, null=True),
        ),
    ]
