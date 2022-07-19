from django.shortcuts import render
from django.http import HttpResponse
from .models import MyProject


def myprojects(request):
    MyProjects = MyProject.objects.all()
    context = {'myprojects': MyProjects}
    return render(request, 'projects/projects.html', context)


def myproject(request, pk):
    myprojectObj = MyProject.objects.get(id=pk)
    return render(request, 'projects/single-project.html', {'myproject': myprojectObj})


def createProject(request):
    context = {}
    return render(request, "projects/project_form.html")

# Create your views here
