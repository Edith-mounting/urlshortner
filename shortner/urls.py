from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('create', views.Createurl, name = 'Createurl'),
    path('<str:pk>', views.go, name = 'go')
]