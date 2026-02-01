from django.urls import path, include
from shohojit import views

urlpatterns = [
    path('', views.index, name='index'),
]
