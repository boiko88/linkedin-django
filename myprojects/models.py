from django.db import models
import uuid

# Create your models here.


class MyProject (models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    demo_link = models.CharField(max_length=200, null=True, blank=True)
    source_code = models.CharField(max_length=2000, null=True, blank=True)
    created_value = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False, primary_key=True)
    
    def __str__(self):
        return self.title
    