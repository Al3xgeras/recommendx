from django.shortcuts import render
from . import templates

def Homepage(request):
    return render(request, 'main/index.html')
