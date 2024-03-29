# Generated by Django 4.2.6 on 2024-02-19 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0050_alter_task_detail_doc_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task_detail',
            name='billstatus',
            field=models.CharField(blank=True, choices=[('Billed', 'Billed'), ('Unbilled', 'Unbilled')], default='Unbilled', max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='task_detail',
            name='doc_type',
            field=models.CharField(blank=True, choices=[('Incoming', 'Incoming'), ('Outgoing', 'Outgoing'), ('Others', 'Others')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='task_detail',
            name='mail_type',
            field=models.CharField(blank=True, choices=[('IPO', 'IPO'), ('Mail', 'Mail'), ('Court', 'Court'), ('Email', 'Email'), ('Personal', 'Personal')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='task_detail',
            name='tran_type',
            field=models.CharField(blank=True, choices=[('Billable', 'Billable'), ('Non-Billable', 'Non-Billable')], max_length=15, null=True),
        ),
    ]
