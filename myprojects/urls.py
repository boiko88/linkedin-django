from django.urls import path
from . import views

urlpatterns = [
    path('', views.myprojects, name="projects"),
    path('myproject/<str:pk>', views.myproject, name="master_link_project"),
]