from django.shortcuts import render
from . import templates

def Homepage(request):
    return render(request, 'index.html')
