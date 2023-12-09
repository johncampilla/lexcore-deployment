from django.urls import path
from . import views

urlpatterns = [
    # path('activity/', views.DocketingListView, name='task-list'),
    path('activity/', views.matterlist, name='task-list'),
    path("activity/add/<int:mid>/'", views.NewActivity, name='new-activity'),
    path("activity/del/<int:pk>/<int:mid>/'", views.RemoveActivity, name='delete-activity'),
    path("activity/edit/<int:pk>/<int:mid>/'", views.EditActivity, name='edit-activity'),
    
]