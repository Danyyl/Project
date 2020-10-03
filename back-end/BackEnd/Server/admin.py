from django.contrib import admin
from Server import models
# Register your models here.
admin.site.register(models.Task)
admin.site.register(models.TaskList)
admin.site.register(models.Session)
admin.site.register(models.Message)