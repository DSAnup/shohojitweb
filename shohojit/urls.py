from django.urls import path, include
from shohojit import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('teams/', views.teams, name='teams'),
    path('courses/', views.courses, name='courses'),
    path('courses/<str:course_slug>/', views.course_detail, name='course_detail'),
    path('gallery/', views.gallery, name='gallery'),
    path('services/', views.services, name='services'),
    path('services/<int:service_id>/', views.service_detail, name='service_detail'),
    path('contact/', views.contact, name='contact'),
]
