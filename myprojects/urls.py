from django.urls import path
from . import views

urlpatterns = [
    path('myprojects/', views.myprojects, name="projects"),
    path('myproject/<str:pk>', views.myproject, name="projects"),
]