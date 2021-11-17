from django.shortcuts import render
from .models import Review

def homepage(request):
    top_reviews = Review.objects.all().order_by('-rating')
    latest_reviews = Review.objects.all().order_by('-date')
    return render(request, 'main/index.html', {'top_reviews':top_reviews, 
                                            'latest_reviews':latest_reviews})

def login(request):
    return render(request, 'main/login.html', {'title': 'Login'})