from django import forms
from .models import *
from django.forms.widgets import NumberInput, TextInput, Textarea, Widget

class InvoiceForm(forms.ModelForm):
    class Meta:
        model = AccountsReceivable
        fields = '__all__'
        widgets = {
            'matter': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'bill_no': forms.TextInput(attrs={'class': 'form-control'}),
            'bill_date': NumberInput(attrs={'type': 'date','class':'form-control'}),
            'total_USDamount': NumberInput(attrs={"class": "form-control", "inputmode": "decimal"}),
            'total_PhPamount': NumberInput(attrs={"class": "form-control", "inputmode": "decimal"}),
            'pf_amount': NumberInput(attrs={"class": "form-control", "inputmode": "decimal"}),
            'filing_amount': NumberInput(attrs={"class": "form-control", "inputmode": "decimal"}),
            'ope_amount': NumberInput(attrs={"class": "form-control", "inputmode": "decimal"}),
            'peso_rate_used': NumberInput(attrs={"class": "form-control", "inputmode": "decimal"}),
            'payment_tag': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
        }

