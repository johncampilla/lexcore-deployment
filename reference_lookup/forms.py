from typing import Any
from django import forms
from taskcode_settings.models import ActivityCodes
from .models import *
from client.models import NatureOfBusiness
from casefolder.models import FolderType

from django.forms.widgets import NumberInput, TextInput, Textarea, Widget


class IndustryForm(forms.ModelForm):
    class Meta:
        model = NatureOfBusiness
        fields = '__all__'
        widgets = {
            'industry': forms.TextInput(attrs={'class': 'form-control'}),
        }

class AppTypeForm(forms.ModelForm):
    class Meta:
        model = AppType
        fields = '__all__'
        widgets = {
            'apptype': forms.TextInput(attrs={'class': 'form-control'}),
        }

class FolderTypeForm(forms.ModelForm):
    class Meta:
        model = FolderType
        fields = '__all__'
        widgets = {
            'folder': forms.TextInput(attrs={'class': 'form-control'}),
        }

class CaseTypeForm(forms.ModelForm):
    class Meta:
        model = CaseType
        fields = '__all__'
        widgets = {
            'case_type': forms.TextInput(attrs={'class': 'form-control'}),
        }

class NatureForm(forms.ModelForm):
    class Meta:
        model = NatureOfCase
        fields = '__all__'
        widgets = {
            'casetype': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'nature': forms.TextInput(attrs={'class': 'form-control'}),
        }

class AppearanceForm(forms.ModelForm):
    class Meta:
        model = Appearance
        fields = '__all__'
        widgets = {
            'appearance': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ActivityCodeForm(forms.ModelForm):
    class Meta:
        model = ActivityCodes
        fields = '__all__'
        widgets = {
            'foldertype': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'ActivityCode': forms.TextInput(attrs={'class': 'form-control'}),
            'ActivityCode': forms.TextInput(attrs={'class': 'form-control'}),
            'TranType': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'Activity': forms.Textarea(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'bill_description': forms.Textarea(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'amount': NumberInput(attrs={"class": "form-control", "inputmode": "decimal"}),
            'currency': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'pesorate': NumberInput(attrs={"class": "form-control", "inputmode": "decimal"}),
            'pesoamount': NumberInput(attrs={"class": "form-control", "inputmode": "decimal"}),
        }

class CourtsCodeForm(forms.ModelForm):
    class Meta:
        model = Courts
        fields = '__all__'
        widgets = {
            'court': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'contact_person': forms.TextInput(attrs={'class': 'form-control'}),
            'contact_number': forms.TextInput(attrs={'class': 'form-control'}),
            'presiding_judge': forms.TextInput(attrs={'class': 'form-control'}),
            'remarks': forms.TextInput(attrs={'class': 'form-control'}),
        }
