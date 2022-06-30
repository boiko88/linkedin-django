
from django.contrib import admin
from django.http import HttpRequest, HttpResponse
from django.urls import path
from django.http import HttpResponse


def myprojects(request):
    return HttpResponse('It actually works!')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('myprojects/', myprojects, name="projects"),
]
