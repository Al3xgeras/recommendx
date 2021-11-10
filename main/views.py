from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Review

class Homepage(ListView):
    model = Review
    template_name = 'main/index.html'
    ordering = ['-rating']