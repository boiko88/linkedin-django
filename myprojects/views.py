from django.shortcuts import render
from django.http import HttpResponse

def myprojects(request):
    return HttpResponse('It actually works!')

def myproject(request, pk):
    return HttpResponse('Single Project!')

# Create your views here.
