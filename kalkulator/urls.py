from django.conf.urls import include
from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.viewpog)
]