from typing import Any
from django import forms
from .models import *
from django.core.exceptions import ValidationError
from django.forms.widgets import NumberInput, TextInput, Textarea, Widget

class MatterForm(forms.ModelForm):
    class Meta:
        model = Matters
        fields = 'folder', 'matter_title', 'appearance', 'matter_contact_person', 'handling_lawyer','opposing_counsel', 'status', 'apptype', 'clientrefno', 'referenceno', 'filing_date', 'matterno', 'case_type', 'filed_at', 'nature', 'lawyers_involve', 'remarks'
        widgets = {
            'folder': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'matter_title': forms.Textarea(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'appearance': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'matter_contact_person': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'handling_lawyer': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'opposing_counsel': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'apptype': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'clientrefno': forms.TextInput(attrs={'class': 'form-control'}),
            'referenceno': forms.TextInput(attrs={'class': 'form-control'}),
            'filing_date': NumberInput(attrs={'type': 'date','class':'form-control'}),
            'matterno': forms.TextInput(attrs={'class': 'form-control'}),
            'case_type': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'filed_at': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'nature': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'lawyers_involve': forms.TextInput(attrs={'class': 'form-control'}),
            'remarks': forms.Textarea(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
        }
class DueDateForm(forms.ModelForm):
    class Meta:
        model = AppDueDate
        fields = 'duecode', 'duedate', 'particulars', 'date_complied'
        widgets = {
#            'matter': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'duecode': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'duedate': NumberInput(attrs={'type': 'date','class':'form-control'}),
            'particulars': forms.Textarea(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),  
            'date_complied': NumberInput(attrs={'type': 'date','class':'form-control'}),
        }

class ApplicantForm(forms.ModelForm):
    class Meta:
        model = Matter_Applicant
        fields = 'main_applicant', 'applicant', 'remarks' 
        widgets = {
#            'matter': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'main_applicant': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'applicant': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'remarks': forms.Textarea(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),  
        }

class ApplicantProfileForm(forms.ModelForm):
    class Meta:
        model  =  Applicant
        fields = 'applicant', 'category', 'entity_type', 'position', 'sex', 'first_name', 'middle_name', 'last_name', 'contact_no', 'email', 'nationality', 'applicant_isinventor', 'address', 'city', 'state', 'country', 'zipcode'
        widgets = {
#            'matter': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'applicant': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'entity_type': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'position': forms.TextInput(attrs={'class': 'form-control'}),
            'sex': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'middle_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'contact_no': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'nationality': forms.TextInput(attrs={'class': 'form-control'}),
            'applicant_isinventor': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.TextInput(attrs={'class': 'form-control'}),
            'country': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'zipcode': forms.TextInput(attrs={'class': 'form-control'}),
        }

class NewCaseDescriptionForm(forms.ModelForm):
    class Meta:
        model = CaseDescription
        fields = 'case_description', 'case_theory', 'submittedby'
        widgets = {
            'case_description': forms.Textarea(attrs={'class': 'form-control', 'cols': 200, 'rows': 3}),  
            'case_theory': forms.Textarea(attrs={'class': 'form-control', 'cols': 200, 'rows': 3}),  
            'submittedby': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),

        }

class NewCaseEvidenceForm(forms.ModelForm):
    class Meta:
        model = CaseEvidence
        fields = 'date_submitted', 'source_evidence', 'evidence_description', 'evidence_file'
        widgets = {
            'date_submitted': NumberInput(attrs={'type': 'date','class':'form-control'}),
            'source_evidence': forms.Textarea(attrs={'class': 'form-control', 'cols': 200, 'rows': 3}),  
            'evidence_description': forms.Textarea(attrs={'class': 'form-control', 'cols': 200, 'rows': 3}),  

        }
class NewPriorityForm(forms.ModelForm):
    class Meta:
        model = ConventionPriority
        fields= 'priority_number', 'priority_date', 'priority_country_filing', 'certified_copy_attached'
        widget = {
            'priority_number': forms.TextInput(attrs={'class': 'form-control'}),
            'priority_date': NumberInput(attrs={'type': 'date','class':'form-control'}),
            'priority_country_filing': forms.TextInput(attrs={'class': 'form-control'}),
            'certified_copy_attached': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 1}),
        }

    