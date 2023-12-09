from django.shortcuts import render, redirect
from .models import *
from .forms import InvoiceForm

# Create your views here.
def InvoiceList(request):
    invoice = AccountsReceivable.objects.all()
    # if request.method == "POST":
    #     form = InvoiceForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('invoice-index')
    #     else:
    #         form = InvoiceForm()
    # else:
    #     form = InvoiceForm()

    context = {
        'invoices' : invoice,
        # 'form':form,
    }
    return render(request, 'invoice/invoice_list.html', context)

def EditInvoice(request, pk):
    pf = AccountsReceivable.objects.get(id=pk)
    bills = Bills.objects.filter(ar__id = pk)
    filing_fees = FilingFees.objects.filter(ar__id = pk)
    print(filing_fees)
    sid = pk
    if request.method == 'POST':
        form = InvoiceForm(request.POST, instance=pf)
        if form.is_valid():
            form.save()
            return redirect('invoice-index')
        else:
            form = InvoiceForm(instance=pf)
    else:
        form = InvoiceForm(instance=pf)

    context = {
        'form': form,
        'bills': bills,
        'filings': filing_fees,
    }
    return render(request, 'invoice/editinvoice.html', context)

def NewInvoice(request):
    if request.method == 'POST':
        form = InvoiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('invoice-index')
        else:
            form = InvoiceForm()
    else:
        form = InvoiceForm()

    context = {
        'form': form,
    }
    return render(request, 'invoice/editinvoice.html', context)

