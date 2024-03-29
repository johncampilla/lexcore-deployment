# Generated by Django 4.2.6 on 2024-01-22 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0031_alter_task_detail_doc_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task_detail',
            name='mail_type',
            field=models.CharField(blank=True, choices=[('Email', 'Email'), ('IPO', 'IPO'), ('Court', 'Court'), ('Mail', 'Mail'), ('Personal', 'Personal')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='task_detail',
            name='tran_type',
            field=models.CharField(blank=True, choices=[('Non-Billable', 'Non-Billable'), ('Billable', 'Billable')], max_length=15, null=True),
        ),
    ]
