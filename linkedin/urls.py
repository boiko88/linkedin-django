
from django.contrib import admin
from django.http import HttpRequest, HttpResponse
from django.urls import path, include





urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myprojects.urls'))
]
