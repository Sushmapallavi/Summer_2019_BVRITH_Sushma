from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from onlineapp.models import *
from django.shortcuts import render

class StudentView(LoginRequiredMixin,View):
    login_url = '/login/'
    def get(selfself,request,*args,**kwargs):
        marks = MockTest1.objects.values('problem1','problem2','problem3','problem4','student_id').filter(student__id=kwargs['id'])
        return render(request,'mocktest.html',{'s':marks})