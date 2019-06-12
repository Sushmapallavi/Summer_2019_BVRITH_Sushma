from django.shortcuts import render
from django.http import HttpResponse
from onlineapp.models import College,Student


# Create your views here.
def hello_world(request):
    #string = "<h1>hello world</h1>"
    #return HttpResponse(College.objects.filter(acronym='bvrith').values('name'))
    return render(request,'hello.html')

def get_all_colleges(request):
    c = College.objects.values('name','acronym')
    #return HttpResponse(c)
    return render(request,'colleges.html',{'k':c})

def students(request,id):
   stud = Student.objects.values_list('id','name','Mocktest1__total').filter(college_id=id)
   return render(request,'marks.html',{'s':stud})



