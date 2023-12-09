from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from activity.models import task_detail
from .forms import *
from casefolder.forms import *
from django.urls import reverse, reverse_lazy
from django.contrib import messages
import string

# Create your views here.

def MatterList(request):
    matters = Matters.objects.all().order_by("-created_at")
    context = {
        'matters' : matters, 
    }
    return render(request, 'matter/index.html', context)

def SelectMatter(request, pk):
    matter = Matters.objects.get(id=pk)
    duedates = AppDueDate.objects.filter(matter_id = pk)
    sid = matter.case_type.id
    stype = CaseType.objects.get(id=sid)
    apptype_id = matter.apptype.id
    sapptype = AppType.objects.get(id=apptype_id)

    #print(stype.case_type)
    
    try:
        ip_matter = IP_Matter.objects.get(matter_id = pk)
    except IP_Matter.DoesNotExist:
        ip_matter = None

    activities = task_detail.objects.filter(matter_id = pk)
    casetheory = CaseDescription.objects.filter(matter_id = pk)
    caseevidence = CaseEvidence.objects.filter(matter_id = pk)
    priorityclaims = ConventionPriority.objects.filter(matter_id = pk)
    applicants = Matter_Applicant.objects.filter(matter_id = pk)
    inventors = Matter_Inventor.objects.filter(matter_id = pk)
    services = Matter_ClassOfGoods.objects.filter(matter_id = pk)

    # if request.method == 'POST':
    #     form = DueDateForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('select-matter', pk)
    #     else:
    #         form = DueDateForm()
    # else:
    #     form = DueDateForm()
    
    context = {
            'matter' : matter,
            'duedates' : duedates,
            'ip_matter' : ip_matter, 
            'activities' : activities,
            'casetheory' : casetheory,
            'caseevidence'  : caseevidence,
            'priorityclaims' : priorityclaims,
            'applicants' : applicants,
            'inventors' : inventors,
            'services': services

#            'form'  : form,
        }
    if stype.case_type == 'IP':
        if sapptype.apptype == "TRADEMARK" : 
            return render(request, 'matter/matter_detail_ip_TM.html', context)
        elif sapptype.apptype == "INVENTION" :
            return render(request, 'matter/matter_detail_ip_INV.html', context)
        elif sapptype.apptype == "PCT" :
            return render(request, 'matter/matter_detail_ip_INV.html', context)
        else :
            return render(request, 'matter/matter_detail_nonip.html', context)

    else:
        return render(request, 'matter/matter_detail_nonip.html', context)
    
        

def newfolder(request):
    if request.method == 'POST':
        form = CaseFolderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('new-matter')
        else:
            form = CaseFolderForm()
    else:
        form = CaseFolderForm()
    
    context = {
        'form':form,
    }
    return render(request, 'matter/newfolder.html', context)

def NewMatter(request):
    if request.method == 'POST':
        form = MatterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('invoice-index')
        else:
            form = MatterForm()
    else:
        form = MatterForm()

    context = {
        'form': form,
    }
    return render(request, 'matter/new_matter_detail.html', context)   

def NewDueDate(request, mid):
    matter = Matters.objects.get(id=mid)
    if request.method == 'POST':
        form = DueDateForm(request.POST)
        if form.is_valid():
            duedate_rec = form.save(commit=False)
            duedate_rec.matter_id = matter.id
            duedate_rec.save()            
            form.save()
            return redirect('select-matter', mid)
        else:
            print('invalid ang form pre 1')
            form = DueDateForm()
    else:
        print('invalid ang form pre 2')
        form = DueDateForm()

    context = {
        'form': form,
        'matter':matter,
    }
    return render(request, 'matter/newduedate.html', context)   

def EditDueDate(request, pk, mid):
    duedate = AppDueDate.objects.get(id=pk)
    sid = mid
    matter = Matters.objects.get(id=mid)
    if request.method == 'POST':
        form = DueDateForm(request.POST, instance=duedate)
        if form.is_valid():
            form.save()
            return redirect('select-matter', mid)
        else:
            form = DueDateForm(instance=duedate)
    else:
        form = DueDateForm(instance=duedate)

    context = {
        'form': form,
        'sid': sid,
        'matter':matter,
    }
    return render(request, 'matter/editduedate.html', context)

def RemoveDueDate(request, pk, mid):
    duedate = AppDueDate.objects.get(id=pk)
    duedate.delete()
    return redirect('select-matter', mid)

def NewApplicant(request, mid):
    matter = Matters.objects.get(id=mid)
    if request.method == 'POST':
        form = ApplicantForm(request.POST)
        if form.is_valid():
            duedate_rec = form.save(commit=False)
            duedate_rec.matter_id = matter.id
            duedate_rec.save()            
            form.save()
            return redirect('select-matter', mid)
        else:
            print('invalid ang form pre 1')
            form = ApplicantForm()
    else:
        print('invalid ang form pre 2')
        form = ApplicantForm()

    context = {
        'form': form,
        'matter':matter,
    }
    return render(request, 'matter/newapplicant.html', context)   

def EditMatterApplicant(request, pk, mid):
    applicant = Matter_Applicant.objects.get(id=pk)
    sid = mid
    matter = Matters.objects.get(id=mid)
    if request.method == 'POST':
        form = ApplicantForm(request.POST, instance=applicant)
        if form.is_valid():
            form.save()
            return redirect('select-matter', mid)
        else:
            form = ApplicantForm(instance=applicant)
    else:
        form = ApplicantForm(instance=applicant)

    context = {
        'form': form,
        'sid': sid,
        'matter':matter,
        'applicant': applicant
    }
    return render(request, 'matter/newapplicant.html', context)   

def NewApplicantProfile(request, mid):
    applicantlist = Applicant.objects.all().order_by('applicant')
    if request.method == 'POST':
        form = ApplicantProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('new-applicantprofile', mid)
        else:
            print('invalid ang form pre 1')
            form = ApplicantProfileForm()
    else:
        print('invalid ang form pre 2')
        form = ApplicantProfileForm()

    context = {
        'form': form,
        'applicantlist':applicantlist,
        'mid':mid,
    }
    return render(request, 'matter/newapplicantprofile.html', context)   

def EditApplicant(request, pk, mid):
    applicant = Applicant.objects.get(id=pk)
    sid = mid
    matter = Matters.objects.get(id=mid)
    if request.method == 'POST':
        form = ApplicantProfileForm(request.POST, instance=applicant)
        if form.is_valid():
            form.save()
            return redirect('select-matter', mid)
        else:
            form = ApplicantProfileForm(instance=applicant)
    else:
        form = ApplicantProfileForm(instance=applicant)

    context = {
        'form': form,
        'sid': sid,
        'matter':matter,
        'applicant': applicant
    }
    return render(request, 'matter/editapplicant.html', context)

def NewCaseDescription(request, mid):
    matter = Matters.objects.get(id=mid)
    if request.method == 'POST':
        form = NewCaseDescriptionForm(request.POST)
        if form.is_valid():
            casedescription_rec = form.save(commit=False)
            casedescription_rec.matter_id = matter.id
            casedescription_rec.save()            
            form.save()
            return redirect('select-matter', mid)
        else:
            print('invalid ang form pre 1')
            form = NewCaseDescriptionForm()
    else:
#        print('invalid ang form pre 2')
        form = NewCaseDescriptionForm()

    context = {
        'form': form,
        'matter':matter,
    }
    return render(request, 'matter/newcasedescription.html', context)   

def NewCaseEvidence(request, mid):
    matter = Matters.objects.get(id=mid)
    if request.method == 'POST':
        form = NewCaseEvidenceForm(request.POST, request.FILES)
        if form.is_valid():
            caseeveidence_rec = form.save(commit=False)
            caseeveidence_rec.matter_id = matter.id
            caseeveidence_rec.save()            
            form.save()
            return redirect('select-matter', mid)
        else:
            print('invalid ang form pre 1')
            form = NewCaseEvidenceForm()
    else:
#        print('invalid ang form pre 2')
        form = NewCaseEvidenceForm()

    context = {
        'form': form,
        'matter':matter,
    }
    return render(request, 'matter/newcaseEvidence.html', context)   

def ViewEvidence(request, pk, mid):
    evidence = CaseEvidence.objects.get(id=pk)
    matter = Matters.objects.get(id=mid)
    form = NewCaseEvidenceForm(instance=evidence)
    if request.method == "POST":
        form = NewCaseEvidenceForm(request.POST, request.FILES, instance=evidence)
        if form.is_valid():
            print("pumasok sa saving pre")
            form.save()
            return redirect('select-matter', mid)
        else:
            form = NewCaseEvidenceForm(instance=evidence)
    else:
        form = NewCaseEvidenceForm(instance=evidence)

    context = {
        'evidence':evidence,
        'matter':matter,
        'form' : form,
    }
    return render(request, 'matter/viewevidence.html', context)

def NewPriority(request, mid):
    matter = Matters.objects.get(id=mid)
    if request.method == 'POST':
        form = NewPriorityForm(request.POST)
        if form.is_valid():
            priority_rec = form.save(commit=False)
            priority_rec.matter_id = matter.id
            priority_rec.save()            
            form.save()
            return redirect('select-matter', mid)
        else:
            print('invalid ang form pre 1')
            form = NewPriorityForm()
    else:
        print('invalid ang form pre 2')
        form = NewPriorityForm()

    context = {
        'form': form,
        'matter':matter,
    }
    return render(request, 'matter/new_priority.html', context)



            


# def viewdocument(request, pk):
#     docs = FilingDocs.objects.get(id=pk)
#     t_id = docs.Task_Detail.id
#     form = DocumentEditForm(instance=docs)
#     lawyer = docs.Task_Detail.lawyer
#     matterid = docs.Task_Detail.matter.id
#     matter = Matters.objects.get(id=matterid)

#     if request.method == "POST":
#         form = DocumentEditForm(request.POST, request.FILES, instance=docs)
#         if form.is_valid():
#             form.save()
#             return redirect('associate-home')
#         else:
#             form = DocumentEditForm(instance=docs)
#     else:
#         form = DocumentEditForm(instance=docs)
        
#     context = {
#         'form' : form,
#         'docs' : docs,
#         'lawyer': lawyer,
#         'matter': matter,
#         't_id': t_id,
#         'm_id': matterid,

#     }

#     return render(request, 'associates_apps/documentview.html', context)
