from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import CaseFolder
from matter.models import Matters
#from django.views.generic import ListView, FormView
from .forms import CaseFolderForm
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.db.models import Q, Sum, Count

import string

def folderlist(request):
    folder_result = Matters.objects.values('folder__folder_type__id', 'folder__folder_type__folder').annotate(NoOfMatters=Count('matter_title'))
    #print(folder_result)
    #.filter(folder__client_id = pk).order_by('-NoOfMatters')
    context = {
        'folders' : folder_result,
    }
    return render(request, 'casefolder/foldercount.html', context)

def selectedfolder(request, pk):
    matters = Matters.objects.filter(folder__folder_type__id = pk)
    context = {
        'matters':matters,
    }

    return render(request, 'casefolder/matterlist.html', context)









# Create your views here.
# class FolderListView(FormView, ListView):
#     template_name = 'casefolder/index.html'
#     context_object_name = 'folders'
#     ordering = '-created_at'
#     form_class = CaseFolderForm
#     # success_url = reverse_lazy('client:client-index')
#     def get_success_url(self):
#         return self.request.path

#     def get_queryset(self):
#         parameter = ''
#         return CaseFolder.objects.filter(folder_description__startswith=parameter).order_by('folder_type', 'client__client_name')

#     # def get_context_data(self, **kwargs):
#     #     context = super().get_context_data(**kwargs)
#     #     return context

#     def get_context_data(self):
#         # letters = list(string.ascii_uppercase)
#         # selected_letter = self.kwargs.get('letter') if self.kwargs.get('letter') else 'a'
#         context = {
#             'form':self.get_form_class(),
#             'folders': self.get_queryset(),
#         }
#         # print('selected_letter', selected_letter)
#         return context

#     def form_valid(self, form):
#         #form.save()
#         self.instance = form.save()
#         messages.add_message(self.request, messages.INFO, f"Case Folder: {self.instance.folder_description } has been created")
#         return super().form_valid(form)

#     def form_invalid(self, form):
#         self.object_list = self.get_queryset()
#         messages.add_message(self.request, messages.ERROR, form.errors)

#         return super().form_invalid(form)
