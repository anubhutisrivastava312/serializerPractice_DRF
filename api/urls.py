from django.urls import path
from django.contrib import admin
from api import views

urlpatterns = [
    
    # path('',views.studentDetails,name=""),
    path('',views.studentDetails_queryset,name=""),
]