from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Review
from django.contrib.auth.forms import UserCreationForm

class Homepage(ListView):
    model = Review
    template_name = 'main/index.html'
    ordering = ['-rating']

def register(request):
    form = UserCreationForm
    return render(request, 'main/register.html', context={'form':form})