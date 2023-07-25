from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('another/', views.another, name='another'),
    path('delete_info/', views.delete_info, name='delete_info'),
]
