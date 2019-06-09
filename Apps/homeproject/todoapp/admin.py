from django.contrib import admin
from . import models


# Register your models here.
admin.site.register(models.todolist)
admin.site.register(models.todoitem)

