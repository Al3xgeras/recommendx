from django.urls import path
from .views import Homepage, register
from . import views

urlpatterns = [
    path('', Homepage.as_view(), name = 'homepage'),
    path('register/', views.register, name='register')
]
