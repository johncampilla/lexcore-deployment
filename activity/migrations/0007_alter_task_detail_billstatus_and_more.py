# Generated by Django 4.2.6 on 2023-11-15 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0006_alter_task_detail_doc_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task_detail',
            name='billstatus',
            field=models.CharField(blank=True, choices=[('Unbilled', 'Unbilled'), ('Billed', 'Billed')], default='Unbilled', max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='task_detail',
            name='doc_type',
            field=models.CharField(blank=True, choices=[('Incoming', 'Incoming'), ('Outgoing', 'Outgoing'), ('Others', 'Others')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='task_detail',
            name='mail_type',
            field=models.CharField(blank=True, choices=[('Mail', 'Mail'), ('Court', 'Court'), ('Personal', 'Personal'), ('Email', 'Email'), ('IPO', 'IPO')], max_length=15, null=True),
        ),
    ]
