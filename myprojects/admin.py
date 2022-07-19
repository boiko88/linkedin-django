from django.contrib import admin

# Register your models here.

from .models import MyProject, Review, Tag


admin.site.register(MyProject)
admin.site.register(Review)
admin.site.register(Tag)
