from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('sendMessage/', views.message),
    path('getData/', views.getData),
]
