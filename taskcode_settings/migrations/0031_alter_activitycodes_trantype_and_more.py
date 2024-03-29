# Generated by Django 4.2.6 on 2024-01-22 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskcode_settings', '0030_alter_duecode_basisofcompute_alter_duecode_fieldbsis'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activitycodes',
            name='TranType',
            field=models.CharField(blank=True, choices=[('BILLABLE', 'BILLABLE'), ('MAILSIN', 'MAILSIN')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='duecode',
            name='basisofcompute',
            field=models.CharField(blank=True, choices=[('In Months', 'In Months'), ('In Days', 'In Days'), ('In Years', 'In Years')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='duecode',
            name='fieldbsis',
            field=models.CharField(blank=True, choices=[('Application Date', 'Application Date'), ('Renewal Date', 'Renewal Date'), ('IR Renewal Date', 'IR Renewal Date'), ('Document Date', 'Document Date'), ('Registration Date', 'RegistrationDate'), ('Publication Date', 'PublicationDate'), ('Priority Date', 'Priority Date'), ('IR Date', 'IR Date'), ('Document Receipt Date', 'Document Receipt Date'), ('PCT Filing Date', 'PCT Filing Date'), ('OA Mailing Date', 'OA Mailing Date'), ('PCT Publication Date', 'PCT Publication Date')], max_length=30, null=True),
        ),
    ]
