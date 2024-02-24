# Generated by Django 4.2.6 on 2024-01-14 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskcode_settings', '0020_alter_activitycodes_trantype_and_more'),
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
            field=models.CharField(blank=True, choices=[('In Days', 'In Days'), ('In Years', 'In Years'), ('In Months', 'In Months')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='duecode',
            name='fieldbsis',
            field=models.CharField(blank=True, choices=[('Application Date', 'Application Date'), ('Renewal Date', 'Renewal Date'), ('Priority Date', 'Priority Date'), ('Registration Date', 'RegistrationDate'), ('Document Date', 'Document Date'), ('OA Mailing Date', 'OA Mailing Date'), ('Publication Date', 'PublicationDate'), ('PCT Filing Date', 'PCT Filing Date'), ('PCT Publication Date', 'PCT Publication Date'), ('Document Receipt Date', 'Document Receipt Date')], max_length=30, null=True),
        ),
    ]
