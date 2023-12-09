from django.shortcuts import render, redirect
from . models import *
from .forms import *
from taskcode_settings.models import ActivityCodes 
from client.models import *

# Create your views here.

def index(request):
    apptype = AppType.objects.all().order_by('apptype')
    industry = NatureOfBusiness.objects.all().order_by('industry')
    currency = Currency.objects.all()
    folder = FolderType.objects.all().order_by('folder')
    nature = NatureOfCase.objects.all().order_by('casetype', 'nature')
    casetype = CaseType.objects.all().order_by('case_type')
    appearance = Appearance.objects.all().order_by('appearance')
    courts = Courts.objects.all().order_by('court')
    taskcodes = ActivityCodes.objects.all().order_by('foldertype', 'ActivityCode')

    context = {
        'apptype': apptype,
        'industry': industry,
        'currency': currency,
        'folder': folder,
        'nature': nature,
        'casetype': casetype,
        'appearance': appearance,
        'courts': courts,
        'taskcodes' : taskcodes
    }
    return render(request, 'reference_lookup/index.html', context)

def newIndustryCode(request):
    if request.method == "POST":
        form = IndustryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reference-index')
        else:
            return redirect('new-industry')
    else:
        form = IndustryForm()

    context = {
        'form': form,
    }

    return render(request, 'reference_lookup/newindustry.html', context)

def EditIndustryCode(request, pk):
    industry = NatureOfBusiness.objects.get(id=pk)
    sid = pk
    if request.method == 'POST':
        form = IndustryForm(request.POST, instance=industry)
        if form.is_valid():
            form.save()
            return redirect('reference-index')
        else:
            form = IndustryForm(instance=industry)
    else:
        form = IndustryForm(instance=industry)

    context = {
        'form': form,
        'sid': sid,
    }
    return render(request, 'reference_lookup/newindustry.html', context)


def NewAppType(request):
    if request.method == "POST":
        form = AppTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reference-index')
        else:
            return redirect('new-industry')
    else:
        form = AppTypeForm()

    context = {
        'form': form,
    }

    return render(request, 'reference_lookup/newapptype.html', context)

def EditAppType(request, pk):
    apptype = AppType.objects.get(id=pk)
    sid = pk
    if request.method == 'POST':
        form = AppTypeForm(request.POST, instance=apptype)
        if form.is_valid():
            form.save()
            return redirect('reference-index')
        else:
            form = AppTypeForm(instance=apptype)
    else:
        form = AppTypeForm(instance=apptype)

    context = {
        'form': form,
        'sid': sid,
    }
    return render(request, 'reference_lookup/newapptype.html', context)


def NewFolderType(request):
    if request.method == "POST":
        form = FolderTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reference-index')
        else:
            return redirect('new-foldertype')
    else:
        form = FolderTypeForm()

    context = {
        'form': form,
    }

    return render(request, 'reference_lookup/newfoldertype.html', context)

def EditFolderType(request, pk):
    folder = FolderType.objects.get(id=pk)
    sid = pk
    if request.method == 'POST':
        form = FolderTypeForm(request.POST, instance=folder)
        if form.is_valid():
            form.save()
            return redirect('reference-index')
        else:
            form = FolderTypeForm(instance=folder)
    else:
        form = FolderTypeForm(instance=folder)

    context = {
        'form': form,
        'sid': sid,
    }
    return render(request, 'reference_lookup/newfoldertype.html', context)

def NewCaseType(request):
    if request.method == "POST":
        form = CaseTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reference-index')
        else:
            return redirect('new-casetype')
    else:
        form = CaseTypeForm()

    context = {
        'form': form,
    }

    return render(request, 'reference_lookup/newCaseType.html', context)

def EditCaseType(request, pk):
    casetype = CaseType.objects.get(id=pk)
    sid = pk
    if request.method == 'POST':
        form = CaseTypeForm(request.POST, instance=casetype)
        if form.is_valid():
            form.save()
            return redirect('reference-index')
        else:
            form = CaseTypeForm(instance=casetype)
    else:
        form = CaseTypeForm(instance=casetype)

    context = {
        'form': form,
        'sid': sid,
    }
    return render(request, 'reference_lookup/newCaseType.html', context)

def NewNature(request):
    if request.method == "POST":
        form = NatureForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reference-index')
        else:
            return redirect('new-nature')
    else:
        form = NatureForm()

    context = {
        'form': form,
    }

    return render(request, 'reference_lookup/newNature.html', context)

def EditNature(request, pk):
    nature = NatureOfCase.objects.get(id=pk)
    sid = pk
    if request.method == 'POST':
        form = NatureForm(request.POST, instance=nature)
        if form.is_valid():
            form.save()
            return redirect('reference-index')
        else:
            form = NatureForm(instance=nature)
    else:
        form = NatureForm(instance=nature)

    context = {
        'form': form,
        'sid': sid,
    }
    return render(request, 'reference_lookup/newNature.html', context)

def NewAppearance(request):
    if request.method == "POST":
        form = AppearanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reference-index')
        else:
            return redirect('new-taskcode')
    else:
        form = AppearanceForm()

    context = {
        'form': form,
    }

    return render(request, 'reference_lookup/newappearance.html', context)

def EditAppearance(request, pk):
    apperance = Appearance.objects.get(id=pk)
    sid = pk
    if request.method == 'POST':
        form = AppearanceForm(request.POST, instance=apperance)
        if form.is_valid():
            form.save()
            return redirect('reference-index')
        else:
            form = AppearanceForm(instance=apperance)
    else:
        form = AppearanceForm(instance=apperance)

    context = {
        'form': form,
        'sid': sid,
    }
    return render(request, 'reference_lookup/newappearance.html', context)

def NewCourts(request):
    if request.method == "POST":
        form = CourtsCodeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reference-index')
        else:
            return redirect('new-taskcode')
    else:
        form = CourtsCodeForm()

    context = {
        'form': form,
    }

    return render(request, 'reference_lookup/newcourts.html', context)

def EditCourts(request, pk):
    courts = Courts.objects.get(id=pk)
    sid = pk
    if request.method == 'POST':
        form = CourtsCodeForm(request.POST, instance=courts)
        if form.is_valid():
            form.save()
            return redirect('reference-index')
        else:
            form = CourtsCodeForm(instance=courts)
    else:
        form = CourtsCodeForm(instance=courts)

    context = {
        'form': form,
        'sid': sid,
    }
    return render(request, 'reference_lookup/newcourts.html', context)


def NewTaskCode(request):
    if request.method == "POST":
        form = ActivityCodeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reference-index')
        else:
            return redirect('new-taskcode')
    else:
        form = ActivityCodeForm()

    context = {
        'form': form,
    }

    return render(request, 'reference_lookup/newtaskcode.html', context)

def EditTaskCode(request, pk):
    taskcode = ActivityCodes.objects.get(id=pk)
    sid = pk
    if request.method == 'POST':
        form = ActivityCodeForm(request.POST, instance=taskcode)
        if form.is_valid():
            form.save()
            return redirect('reference-index')
        else:
            form = ActivityCodeForm(instance=taskcode)
    else:
        form = ActivityCodeForm(instance=taskcode)

    context = {
        'form': form,
        'sid': sid,
    }
    return render(request, 'reference_lookup/newtaskcode.html', context)

