from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('contacts/', views.contacts, name='contacts'),
    path('appointment/', views.make_an_appointment, name='make_an_appointment'),
    path('resources/', views.resources, name='resources'),
    path('services/', views.services, name='services'),
    # Add more URL patterns as needed
]
