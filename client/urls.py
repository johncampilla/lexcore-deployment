from django.urls import path
from . import views

urlpatterns = [
    path("client/", views.ClientList, name='client-index'),
    path("selectclient/<int:pk>/'", views.SelectClient, name='select-client'),
    path("newclient/", views.newclient, name='new-client'),
    path("viewfoldermatters/<int:pk>/<int:cid>/'", views.viewfoldercount, name='folder-matters'),
    path("newclientmatter/<int:pk>/'", views.newclient_matter, name='newclient-matter'),
    path("editclientmatter/<int:pk>/<int:cid>/'", views.editclientmatter, name='editclient-matter'),
    path("removeclientmatter/<int:pk>/<int:cid>/'", views.removeclientmatter, name='removeclient-matter'),
    
    path("newfolder/", views.newfolder, name='newclient-folder'),
    path("newfoldermatter/<int:pk>/<int:cid>/'", views.newfoldermatter, name='newfolder-matter'),
    
    path("selectfolder/<int:pk>/<int:cid>/'", views.selectfolder, name='select-folder'),
    


    path("editclient/<int:pk>/'", views.editclient, name='edit-client'),
    path("removeclient/<int:pk>/'", views.removeclient, name='remove-client'),

    path("newcontacts/", views.newcontactperson, name='new-contact'),
    path("editcontacts/<int:pk>/<int:cid>/'", views.editclientcontact, name='edit-contact'),
    path("viewcontactdetails/<int:pk>/<int:cid>/<str:contacts>/'", views.viewconnectedclients, name='viewclientdetails-contact'),
    path("viewconnectedmatterdetails/<int:pk>/<int:cid>/<str:contacts>/'", views.viewconnectedmatters, name='viewmatterdetails-contact'),

    path("deletecontact/<int:pk>/<int:cid>/'", views.removecontact, name='remove-contact'),
   
]    
