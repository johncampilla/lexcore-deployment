from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import task_detail
from matter.models import Matters
from .forms import ActivityForm
from django.urls import reverse, reverse_lazy
from django.contrib import messages
import string

# Create your views here.

def DocketingListView(request):
    activities = task_detail.objects.all().order_by('-tran_date')

    context={
        'activities' : activities 
    }

    return render(request, 'activity/index.html', context)

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
            print('invalid ang form pre 1')
            form = ActivityForm()
    else:
        print('invalid ang form pre 2')
        form = ActivityForm()

    context = {
        'form': form,
        'matter':matter,
    }
    return render(request, 'activity/newactivity.html', context)   

def EditActivity(request, pk, mid):
    activity = task_detail.objects.get(id=pk)
    sid = mid
    matter = Matters.objects.get(id=mid)
    if request.method == 'POST':
        form = ActivityForm(request.POST, instance=activity)
        if form.is_valid():
            form.save()
            return redirect('select-matter', mid)
        else:
            form = ActivityForm(instance=activity)
    else:
        form = ActivityForm(instance=activity)

    context = {
        'form': form,
        'sid': sid,
        'matter':matter,
        'activity': activity,
    }
    return render(request, 'activity/editactivity.html', context)

def RemoveActivity(request, pk, mid):
    activity = task_detail.objects.get(id=pk)
    activity.delete()
    return redirect('select-matter', mid)

def matterlist(request):
    matters = Matters.objects.all()

    context = {
        'matters': matters,
    }

    return render(request, 'activity/docketlist.html', context)
    
