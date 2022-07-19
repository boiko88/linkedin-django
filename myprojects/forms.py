from django.forms import ModelForm
from .models import MyProject

class ProjectForm(ModelForm):
    class Meta:
        model = MyProject
        fields = '__all__'