from django.contrib import admin

# Register your models here.

from .models import Store, ProjectInfos

admin.site.register(Store)
admin.site.register(ProjectInfos)