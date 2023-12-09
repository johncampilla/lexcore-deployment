from typing import Any
from django import forms
from .models import CaseFolder
from django.core.exceptions import ValidationError
from django.forms.widgets import NumberInput, TextInput, Textarea, Widget

class CaseFolderForm(forms.ModelForm):
    class Meta:
        model = CaseFolder
        fields = 'client', 'folder_description', 'folder_type', 'Supervisinglawyer', 'remarks'
        widgets = {
            'client': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'folder_description': forms.Textarea(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),            
            'folder_type': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'Supervisinglawyer': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'remarks': forms.Textarea(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
        }

    def clean(self):
        folderdescription = self.cleaned_data.get('folder_description')
        if len(folderdescription) < 1:
            error_msg = 'the folder description is too short'
            raise ValidationError(error_msg)
        
#         matter_name_exist = CaseFolder.objects.filter(folder_description__iexact=folderdescription).exists()
#         if matter_name_exist:
#             error_msg = "The folder description already exist"
#             self.add_error('folder_description', error_msg)
# #            raise ValidationError(error_msg)
         
        return self.cleaned_data        
