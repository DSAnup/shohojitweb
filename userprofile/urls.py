from django.urls import path
from . import views
from administrator.generic_pdf import generate_profile_pdf

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('profile_settings/<int:id>', views.profile_settings, name='profile_settings'),
    path('profile_pdf/<int:pk>/', generate_profile_pdf, name='profile_pdf'),
]
