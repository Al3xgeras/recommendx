from django.urls import path
from . import views    

urlpatterns = [
    path('register/', views.register, name='register'),
    path('settings/', views.profile_settings, name='profile-settings')
]
