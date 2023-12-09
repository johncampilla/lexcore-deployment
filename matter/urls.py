from django.urls import path
from . import views


urlpatterns = [
    path('matters/', views.MatterList, name='matter-list'),
    path("select/<int:pk>/'", views.SelectMatter, name='select-matter'),
    #path("select_ip/<int:pk>/'", views.SelectMatter_ip, name='select-matter_ip'),
    path('newmatter/', views.NewMatter, name='new-matter'),
    path('newfolder/', views.newfolder, name='new-folder'),    


# Due Date Tab functions
    path("duedate/select/<int:pk>/<int:mid>/'", views.EditDueDate, name='edit-duedate'),
    path("duedate/del/<int:pk>/<int:mid>/'", views.RemoveDueDate, name='delete-duedate'),
    path("duedate/select/<int:pk>/<int:mid>/'", views.EditDueDate, name='edit-duedate'),
    path("duedate/add/<int:mid>/'", views.NewDueDate, name='new-duedate'),

# Applicant Tab functions
    path("applicant/add/<int:mid>/'", views.NewApplicant, name='new-applicant'),
    path("applicantlist/add/<int:mid>/'", views.NewApplicantProfile, name='new-applicantprofile'),
    path("applicant/edit/<int:pk>/<int:mid>/'", views.EditApplicant, name='edit-applicant'),
    path("applicantmain/edit/<int:pk>/<int:mid>/'", views.EditMatterApplicant, name='edit-mainapplicant'),

# casedescription tab functions
    path("casedescription/add/<int:mid>/'", views.NewCaseDescription, name='new-casedescription'),

    
# case_evidence tab functions
    path("caseevidence/add/<int:mid>/'", views.NewCaseEvidence, name='new-case_evidence'),
    path("evidence/view/<int:pk>/<int:mid>/'", views.ViewEvidence, name='view-case_evidence'),

# Priority
    path("priority/add/<int:mid>/'", views.NewPriority, name='new-priority'),


# Other Information
#    path("otherinfo/<int:pk>/<str:casetype>/'", views.viewotherinfo, name='otherinfo-bycasetype'),


]
