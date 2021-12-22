from django.contrib import admin
from django.urls import path
from . import views
from .views import Class_View_One

urlpatterns = [

    path('first', views.first),
    path('another', Class_View_One.as_view())
]
