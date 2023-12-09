from django.urls import path
from . import views

urlpatterns = [
    path("reference/", views.index, name='reference-index'),
    path("newtaskcode/", views.NewTaskCode, name='new-taskcode'),
    path('edittaskcode/<int:pk>/', views.EditTaskCode, name='edit-taskcode'),
    path("newindustry/", views.newIndustryCode, name='new-industry'),
    path("editindustry/<int:pk>/'", views.EditIndustryCode, name='edit-industry'),
    path("newapptype/", views.NewAppType, name='new-apptype'),
    path("editapptype/<int:pk>/'", views.EditAppType, name='edit-apptype'),
    path("newfoldertype/", views.NewFolderType, name='new-foldertype'),
    path("editfolder/<int:pk>/'", views.EditFolderType, name='edit-folder'),
    path("newcasetype/", views.NewCaseType, name='new-casetype'),
    path("editcasetype/<int:pk>/'", views.EditCaseType, name='edit-casetype'),
    path("newnature/", views.NewNature, name='new-nature'),
    path("editnature/<int:pk>/'", views.EditNature, name='edit-nature'),
    path("newapperance/", views.NewAppearance, name='new-appearance'),
    path("editappearance/<int:pk>/'", views.EditAppearance, name='edit-appearance'),
    path("newcourts/", views.NewCourts, name='new-courts'),
    path("editcourts/<int:pk>/'", views.EditCourts, name='edit-courts'),

]
