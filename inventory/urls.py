from django.contrib import admin
from django.urls import path, include
from . import views
from inventory import views

urlpatterns = [

    path('',views.insertdata),
    path('check',views.checkuser),
    path('test',views.checkuser),


]
