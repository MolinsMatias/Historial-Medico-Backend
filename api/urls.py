
from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
   path('', views.api_overview, name='api-overview'),
]
