# Generated by Django 4.2.6 on 2024-02-08 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0040_alter_task_detail_mail_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task_detail',
            name='doc_type',
            field=models.CharField(blank=True, choices=[('Others', 'Others'), ('Incoming', 'Incoming'), ('Outgoing', 'Outgoing')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='task_detail',
            name='mail_type',
            field=models.CharField(blank=True, choices=[('IPO', 'IPO'), ('Court', 'Court'), ('Personal', 'Personal'), ('Mail', 'Mail'), ('Email', 'Email')], max_length=15, null=True),
        ),
    ]
