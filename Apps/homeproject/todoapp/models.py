from django.db import models

# Create your models here.

class todolist(models.Model):
    name = models.CharField(max_length=64)
    created = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

class todoitem(models.Model):
    description = models.CharField(max_length=256)
    due_date = models.DateField(null=True,blank=True)
    completed = models.BooleanField(default=False)
    list = models.ForeignKey(todolist, on_delete=models.CASCADE)


