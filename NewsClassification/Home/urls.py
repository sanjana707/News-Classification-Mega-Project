from django.contrib import admin
from django.urls import path, include
from Home import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('news', views.news, name='news'),
    path('contact', views.news, name='contact')
]
