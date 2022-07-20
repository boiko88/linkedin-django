from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import MyProject
from .forms import ProjectForm


def myprojects(request):
    MyProjects = MyProject.objects.all()
    context = {'myprojects': MyProjects}
    return render(request, 'projects/projects.html', context)


def myproject(request, pk):
    myprojectObj = MyProject.objects.get(id=pk)
    return render(request, 'projects/single-project.html', {'myproject': myprojectObj})


def createProject(request):
    form = ProjectForm()
    
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects')
        
def updateProject(request, pk):
    myproject = MyProject.objects.get(id=pk)
    form = ProjectForm(instance=myproject)
    
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=myproject)
        if form.is_valid():
            form.save()
            return redirect('projects')
    
    
    context = {'form': form}
    return render(request, "projects/project_form.html", context)

# Create your views here
