from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import *
from matter.models import Matters, AppDueDate, ConventionPriority
from casefolder.models import CaseFolder
from activity.models import task_detail
from invoice.models import *
from .forms import *
from matter.forms import MatterForm
from casefolder.forms import CaseFolderForm
from client.forms import ClientContactsForm
from django.contrib import messages
from django.db.models import Q, Sum, Count
from datetime import date, datetime, timedelta
import string

today = date.today()

    # if request.method == 'POST':
    #     form = MatterForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('invoice-index')
    #     else:
    #         form = MatterForm()
    # else:
    #     form = MatterForm()

    # context = {
    #     'form': form,
    # }
    # return render(request, 'matter/new_matter_detail.html', context)   

def ClientList(request):

    if 'q' in request.GET:
        q = request.GET['q']
        multiple_q = Q(Q(client_name__icontains=q) | Q(industry__industry__icontains=q) | Q(category__icontains=q) | Q(address__icontains=q) | Q(billing_currency__currency__icontains=q))
        

        clients = Client_Data.objects.filter(multiple_q).order_by("client_name")
        
    else:
        
        clients = Client_Data.objects.all().order_by('-created')


    context = {
        'clients': clients,
    }
    return render(request, 'client/listclients.html', context)


def SelectClient(request, pk):
    client = Client_Data.objects.get(id=pk)
    clientmatters = Matters.objects.filter(folder__client_id = pk)
    folders = CaseFolder.objects.filter(client_id = pk)

    contact_persons = Contact_Person.objects.filter(client_id = pk)
    accounts_receivables = AccountsReceivable.objects.filter(matter__folder__client_id = pk).order_by('-bill_date')
    activities = task_detail.objects.filter(matter__folder__client_id = pk).order_by('-tran_date')
    priorityclaims = ConventionPriority.objects.filter(matter__folder__client_id = pk)
    duedates = AppDueDate.objects.filter(matter__folder__client_id = pk)
    folder_result = Matters.objects.values('folder__folder_type__id', 'folder__folder_type__folder').annotate(
    NoOfMatters=Count('matter_title')).filter(folder__client_id = pk).order_by('-NoOfMatters')
    form = ClientForm()
    formfolder = CaseFolderForm() 
    formcontact = ClientContactsForm()
    context = {
        'matters' : clientmatters,
        'client' : client,
        'folders': folders,
        'contacts': contact_persons,
        'activities' : activities,
        'duedates' : duedates,
        'folder_result': folder_result,
        'accounts_receivables':accounts_receivables,
        'priorityclaims': priorityclaims,
        'form': form,
        'formfolder': formfolder,
        'formcontact': formcontact,
    }

    return render(request, 'client/client_detail.html', context)

def newclient(request):
#    client = Client_Data.objects.get(id=pk)
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            print('Ok naman pala bro!')
            messages.success(request, "Employee has been successfully added!")
            return HttpResponseRedirect('/')
        else:
            form = ClientForm()
    else:
        form = ClientForm()

#     context = {
#         'form' : form,
# #        'client': client,
#     }
#     return render(request, 'client/add_client.html', context)
#            return redirect('select-client', pk)
#            client_rec = form.save(commit=False)
#            client_rec.save()
#            duedate_rec.matter_id = matter.id
#            duedate_rec.save()   


def newclient_matter(request, pk):
    client = Client_Data.objects.get(id = pk)
    if request.method == 'POST':
        form = MatterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('select-client', pk)
        else:
            form = MatterForm()
    else:
        form = MatterForm()
    
    context = {
        'form' : form,
        'client' : client
    }
    return render(request, 'client/newclient_matter.html', context)

def editclientmatter(request, pk, cid):
    matter = Matters.objects.get(id=pk)
    client = Client_Data.objects.get(id=cid)
    if request.method == 'POST':
        form = MatterForm(request.POST, instance=matter)
        if form.is_valid():
            form.save()
            return redirect('select-client', cid)
        else:
            form = MatterForm(instance=matter)
    else:
        form = MatterForm(instance=matter)
    
    context = {
        'form' : form,
        'matter': matter,
        'client': client,
    }
    return render(request, 'client/editclientmatter.html', context)
    
def editclient(request, pk):
    client = Client_Data.objects.get(id = pk)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('select-client', pk)
        else:
            form =  ClientForm(instance=client)
    else:
        form =  ClientForm(instance=client)

    context = {
        'form': form,
        'client':client,
    }
    return render(request, 'client/editclient.html', context)

def removeclientmatter(request, pk, cid):
    matter = Matters.objects.get(id = pk)
    matter.delete()
    return redirect('select-client', cid)

def removeclient(request, pk):
    client = Client_Data.objects.get(id = pk)
    client.delete()
    return redirect('client-index')

def viewfoldercount(request, pk, cid):
    matters = Matters.objects.filter(folder__folder_type__id=pk, folder__client_id = cid).order_by('-created_at')
    client = Client_Data.objects.get(id = cid)

    context = {
        'matters':matters,
        'client' : client,
    }
    return render(request, 'client/folderdetailslist.html', context)

def selectfolder(request, pk, cid):
    matters = Matters.objects.filter(folder_id = pk)
    client = Client_Data.objects.get(id=pk)
    context = {
        'matters': matters,
        'client' : client,

    }
    return render(request, 'client/folderdetailslist.html')


def viewclientactivities(request, pk):
    client = Client_Data.objects.get(id = pk)
    tasks = task_detail.objects.filter(matter__folder__client_id = pk).order_by('-tran_date')

    context = {
        'tasks' : tasks,
    }

    return render(request, 'client/folderdetailslist.html', context)


def newcontactperson(request):
    if request.method == 'POST':
        form = ClientContactsForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    
        
def editclientcontact(request, pk, cid):
    contact = Contact_Person.objects.get(id=pk)
    sid = cid
    client = Client_Data.objects.get(id=cid)
    if request.method == 'POST':
        form = ClientContactsForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('select-client', cid)
        else:
            form = ClientContactsForm(instance=contact)
    else:
        form = ClientContactsForm(instance=contact)

    context = {
        'form': form,
        'sid': sid,
        'contacts' : contact,
        'client':client,
    }
    return render(request, 'client/editclientcontact.html', context)

def removecontact(request, pk, cid):
    contact = Contact_Person.objects.get(id=pk)
    contact.delete()
    return redirect('select-client', cid)

def NewActivity(request, mid):
    matter = Matters.objects.get(id=mid)
    if request.method == 'POST':
        form = ActivityForm(request.POST)
        if form.is_valid():
            activity_rec = form.save(commit=False)
            activity_rec.matter_id = matter.id
            activity_rec.save()            
            form.save()
            return redirect('select-matter', mid)
        else:
            form = ActivityForm()
    else:
        form = ActivityForm()

    context = {
        'form': form,
        'matter':matter,
    }
    return render(request, 'activity/newactivity.html', context)   

def newfolder(request):
    if request.method == 'POST':
        form = CaseFolderForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    
    # context = {
    #     'form':form,
    # }

    # return render(request, 'client/newfolder.html', context)

def newfoldermatter(request, pk, cid):
    casefolder = CaseFolder.objects.get(id = pk)
    client = Client_Data.objects.get(id = cid)

    if request.method == 'POST':
        form = ClientMatterForm(request.POST)
        if form.is_valid():
            matter_rec = form.save(commit=False)
            matter_rec.folder_id = casefolder.id
            matter_rec.save()            
            form.save()
            return redirect('select-client', cid)
        else:
            form = ClientMatterForm()
    else:
        form = ClientMatterForm()
    
    context = {
        'form':form,
        'client': client,
        'casefolder':casefolder,
    }

    return render(request, 'client/newclient_matter.html', context)

def viewconnectedclients(request, pk, cid, contacts):
    client = Client_Data.objects.get(id=cid)
    contactname = contacts
    contacts = Contact_Person.objects.filter(contact_person = contacts)

    context = {
        'client' : client,
        'contacts':contacts,
        'contactname' : contactname
        
    }

    return render(request, 'client/connectedclients.html', context)

def viewconnectedmatters(request, pk, cid, contacts):
    client = Client_Data.objects.get(id=cid)
    matters = Matters.objects.filter(matter_contact_person_id = pk, folder__client_id = cid)
    print(matters)

    context = {
        'client' : client,
        'matters': matters,
        'contacts':contacts,
    }

    return render(request, 'client/connectedmatters.html', context)


# Create your views here.


