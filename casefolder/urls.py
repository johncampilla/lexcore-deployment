from django.urls import path
from . import views

urlpatterns = [
    path('folders/', views.folderlist, name='folder-index'),
    path("foldermatters/<int:pk>/'", views.selectedfolder, name='selected-folder'),
]
