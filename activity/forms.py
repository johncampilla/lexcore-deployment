from typing import Any
from django import forms
from .models import task_detail
from django.core.exceptions import ValidationError
from django.forms.widgets import NumberInput, TextInput, Textarea, Widget

class ActivityForm(forms.ModelForm):
    class Meta:
        model = task_detail
        fields = 'matter','tran_date', 'doc_date', 'mailing_date', 'doc_type', 'stage_group','task_code', 'tran_type','lawyer', 'task', 'spentinhrs', 'spentinmin', 'mail_type', 'duecode', 'contact_person', 'billstatus'
        widgets = {
            'matter': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'tran_date': NumberInput(attrs={'type': 'date','class':'form-control'}),
            'doc_date': NumberInput(attrs={'type': 'date','class':'form-control'}),
            'mailing_date': NumberInput(attrs={'type': 'date','class':'form-control'}),
            'doc_type': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'stage_group': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'task_code': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'tran_type': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'lawyer': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'task': forms.Textarea(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'spentinhrs': NumberInput(attrs={"class": "form-control", "inputmode": "decimal"}),
            'spentinmin': NumberInput(attrs={"class": "form-control", "inputmode": "decimal"}),
            'examiner': forms.TextInput(attrs={'class': 'form-control'}),
            'mail_type': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'duecode': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'billstatus': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2})
        }

    def clean(self):
        task_desc = self.cleaned_data.get('task')
        if len(task_desc) < 1:
            error_msg = 'the activity name is too short'
            raise ValidationError(error_msg)
        
#         task_desc_exist = task_detail.objects.filter(matter_title__iexact=mattertitle).exists()
#         if task_desc_exist:
#             error_msg = "The matter title already exist"
#             self.add_error('matter_title', error_msg)
# #            raise ValidationError(error_msg)
         
        return self.cleaned_data        
