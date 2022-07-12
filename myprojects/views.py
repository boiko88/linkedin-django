from django.shortcuts import render
from django.http import HttpResponse

def myprojects(request):
    msg = 'Hello! You are on the project page!'
    return render(request, 'projects/projects.html', {'message':msg})

def myproject(request, pk):
    return render(request, 'projects/single-project.html')

# Create your views here.
