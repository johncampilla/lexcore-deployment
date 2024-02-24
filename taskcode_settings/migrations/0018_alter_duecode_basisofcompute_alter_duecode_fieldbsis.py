# Generated by Django 4.2.6 on 2023-12-16 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskcode_settings', '0017_alter_duecode_basisofcompute_alter_duecode_fieldbsis'),
    ]

    operations = [
        migrations.AlterField(
            model_name='duecode',
            name='basisofcompute',
            field=models.CharField(blank=True, choices=[('In Years', 'In Years'), ('In Months', 'In Months'), ('In Days', 'In Days')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='duecode',
            name='fieldbsis',
            field=models.CharField(blank=True, choices=[('Publication Date', 'PublicationDate'), ('OA Mailing Date', 'OA Mailing Date'), ('PCT Publication Date', 'PCT Publication Date'), ('Document Date', 'Document Date'), ('Application Date', 'Application Date'), ('Renewal Date', 'Renewal Date'), ('Registration Date', 'RegistrationDate'), ('Priority Date', 'Priority Date'), ('Document Receipt Date', 'Document Receipt Date'), ('PCT Filing Date', 'PCT Filing Date')], max_length=30, null=True),
        ),
    ]
