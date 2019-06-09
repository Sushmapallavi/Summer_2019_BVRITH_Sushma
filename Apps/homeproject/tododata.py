import string
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'homeproject.settings')
django.setup()
from django.conf import settings
from todoapp.models import *

def populate():
    for i in range(1,6):
        lst = todolist(name="todolist"+str(i))
        lst.save()
        for j in range(1,6):
            itm = todoitem(description="todoitem"+str(j),list=lst)
            itm.save()

if __name__ == '__main__':
    populate()