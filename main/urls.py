from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('helloWorld/', views.helloWorld),
    path('', views.landingPage, name='landing-page'),
    path('oi/', views.oi, name='landing-page'),
]
