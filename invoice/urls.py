from django.urls import path
from . import views

urlpatterns = [
    path('invoice/', views.InvoiceList, name='invoice-index'),
    path('newinvoice/', views.NewInvoice, name='new-invoice'),
    path("editinvoice/<int:pk>/'", views.EditInvoice, name='edit-invoice'),

]