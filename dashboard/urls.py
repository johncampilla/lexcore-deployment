from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='dashboard-index'),
    path('details/newmatters', views.details_new_matters, name='dashboard-details-newmatters'),
    path('newtask/', views.newactivity, name='dashboard-addtask'),  
    path('searchlist', views.searchlist, name='dashboard-searchlist'),
    path('reports/', views.reports, name='reports-items'),
    path('totalindustry/', views.totalcountindustry, name='chart-totalindustry'),
    path('totalapptype/', views.totalcountapptype, name='chart-totalapptype'),
    path('totallawyers/', views.totalcountlawyers, name='chart-totallawyers'),
    path('totalfolders/', views.totalcasefolders, name='chart-totalfolders'),
    path('totalcasetype/', views.totalcasetype, name='chart-totalcasetype'),
    path('totalnature/', views.totalnature, name='chart-totalnature'),
    path('printapptype/', views.printapptypecount, name='chart-print-apptype'),
    path('printindustry/', views.printindustrycount, name='chart-print-industry'),
    path('printlawyer/', views.printlawyercount, name='chart-print-lawyer'),
    path('printfolder/', views.printfoldercount, name='chart-print-folder'),
    path('printcasetype/', views.printcasetypecount, name='chart-print-casetype'),
    path('printnature/', views.printnaturecount, name='chart-print-nature'),

    # detail of summary
    path("printlist/<str:selected>/'", views.detailapplicationtype, name='print-selected-apptype'),
    path("printlist_industry/<str:selected>/'", views.detailindustry, name='print-selected-industry'),
    path("printlist_lawyers/<str:selected>/'", views.detaillawyers, name='print-selected-lawyers'),
    path("printlist_folders/<str:selected>/'", views.detailfolders, name='print-selected-folders'),
    path("printlist_casetype/<str:selected>/'", views.detailcasetype, name='print-selected-casetype'),



    
]
