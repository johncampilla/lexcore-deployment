# Generated by Django 4.2.6 on 2024-02-15 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0043_alter_task_detail_billstatus_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task_detail',
            name='doc_type',
            field=models.CharField(blank=True, choices=[('Outgoing', 'Outgoing'), ('Others', 'Others'), ('Incoming', 'Incoming')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='task_detail',
            name='mail_type',
            field=models.CharField(blank=True, choices=[('IPO', 'IPO'), ('Mail', 'Mail'), ('Email', 'Email'), ('Court', 'Court'), ('Personal', 'Personal')], max_length=15, null=True),
        ),
    ]
