from django.forms import ModelForm
from .models import MyProject

class ProjectForm(ModelForm):
    class Meta:
        model = MyProject
        fields = ['title', 'description', 'demo_link', 'source_code', 'tags',]