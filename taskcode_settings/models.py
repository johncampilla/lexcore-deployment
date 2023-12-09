from django.db import models
from client.models import *
from reference_lookup.models import *

# Create your models here.


class ActivityCodes(models.Model):

    TRANTYPE = {
        ('MAILSIN', 'MAILSIN'),
        ('BILLABLE', 'BILLABLE'),
    }

    foldertype = models.ForeignKey(FolderType, on_delete=models.CASCADE)
    ActivityCode = models.CharField(max_length=15, blank=True)
    TranType = models.CharField(
        max_length=15, choices=TRANTYPE, null=True, blank=True)
    seqorder = models.IntegerField(blank=True, null=True)
    Activity = models.CharField(max_length=250)
    bill_description = models.CharField(max_length=250, blank=True, null=True)
    amount = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    currency = models.ForeignKey(
        Currency, on_delete=models.CASCADE, null=True, blank=True)
    pesorate = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True)
    pesoamount = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)


    class Meta:
        verbose_name_plural = 'Task/Activity Codes'
    
    def __str__(self):
        return f"{self.foldertype} - {self.ActivityCode} {self.Activity}"



class DueCode(models.Model):
    SelectBasis = {
        ('In Days', 'In Days'),
        ('In Months', 'In Months'),
        ('In Years', 'In Years'),
    }

    SelectFieldBasis = {
        ('Publication Date', 'PublicationDate'),
        ('Registration Date', 'RegistrationDate'),
        ('Application Date', 'Application Date'),
        ('Priority Date', 'Priority Date'),
        ('PCT Filing Date', 'PCT Filing Date'),
        ('PCT Publication Date', 'PCT Publication Date'),
        ('Renewal Date', 'Renewal Date'),
        ('Document Date', 'Document Date'),
        ('Document Receipt Date', 'Document Receipt Date'),
        ('OA Mailing Date', 'OA Mailing Date'),
    }

    DueCode = models.CharField(max_length=20, blank=True)
    Description = models.CharField(max_length=200, blank=True)
    folder_type = models.ForeignKey(
        FolderType, on_delete=models.CASCADE, null=True, blank=True)
    apptype = models.ForeignKey(
        AppType, on_delete=models.CASCADE, null=True, blank=True)
    basisofcompute = models.CharField(
        max_length=15, choices=SelectBasis, null=True, blank=True)
    fieldbsis = models.CharField(
        max_length=30, choices=SelectFieldBasis, null=True, blank=True)
    terms = models.DecimalField(
        null=True, blank=True, max_digits=5, decimal_places=3)

    def __str__(self):
        return f'{self.DueCode} - {self.apptype} - {self.Description}'
