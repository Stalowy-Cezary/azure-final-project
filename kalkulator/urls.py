from django.conf.urls import include
from django.urls import path
from . import views
from django.contrib import admin

from django.urls import path
from django.views.generic import RedirectView

from . import views


urlpatterns = [
    path('', views.viewpog),
]