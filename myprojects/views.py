from django.shortcuts import render
from django.http import HttpResponse

def myprojects(request):
    return render(request, 'projects.html')

def myproject(request, pk):
    return render(request, 'single-project.html')

# Create your views here.
