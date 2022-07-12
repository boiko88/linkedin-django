from django.shortcuts import render
from django.http import HttpResponse

projectsList = [
    {
     'id': '1',
     'title': 'Ecommerce Website',
     'description': 'Fully functional ecommerce website',   
        
    },
    {
     'id': '2',
     'title': 'Portfolio Website',
     'description': 'Personal Portfolio of the Developer',   
        
    },
    {
     'id': '3',
     'title': 'eLearning Platform',
     'description': 'A Platform for learning English',   
        
    },

]


def myprojects(request):
    page = 'myprojects'
    number = 10
    context = {'page': page, 'number': number, 'myprojects': projectsList}
    return render(request, 'projects/projects.html', context)


def myproject(request, pk):
    return render(request, 'projects/single-project.html')

# Create your views here.
