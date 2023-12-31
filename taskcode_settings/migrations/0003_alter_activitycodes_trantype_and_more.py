# Generated by Django 4.2.6 on 2023-11-13 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskcode_settings', '0002_alter_duecode_basisofcompute_alter_duecode_fieldbsis'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activitycodes',
            name='TranType',
            field=models.CharField(blank=True, choices=[('MAILSIN', 'MAILSIN'), ('BILLABLE', 'BILLABLE')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='duecode',
            name='basisofcompute',
            field=models.CharField(blank=True, choices=[('In Months', 'In Months'), ('In Days', 'In Days'), ('In Years', 'In Years')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='duecode',
            name='fieldbsis',
            field=models.CharField(blank=True, choices=[('OA Mailing Date', 'OA Mailing Date'), ('Publication Date', 'PublicationDate'), ('Registration Date', 'RegistrationDate'), ('PCT Filing Date', 'PCT Filing Date'), ('PCT Publication Date', 'PCT Publication Date'), ('Priority Date', 'Priority Date'), ('Renewal Date', 'Renewal Date'), ('Document Receipt Date', 'Document Receipt Date'), ('Document Date', 'Document Date'), ('Application Date', 'Application Date')], max_length=30, null=True),
        ),
    ]
