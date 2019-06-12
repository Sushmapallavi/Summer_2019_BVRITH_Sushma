from django.views import View
from onlineapp.forms.addstudent import StudentForm
from onlineapp.forms.mocktest import MarksForm
from onlineapp.models import *
from django.shortcuts import render
from django.shortcuts import *
from django.urls import resolve
from onlineapp.views import College


class AddstudentView(View):
    def get(self,request):
        form1 = StudentForm()
        form2 = MarksForm()
        return render(request,"addstudent.html",{'form1':form1,'form2':form2})

    def post(self,request,*args,**kwargs):
        form1 = StudentForm(request.POST)
        form2 = MarksForm(request.POST)
        if form1.is_valid() and form2.is_valid():
            return HttpResponse(**kwargs)
            student = form1.save(commit=False)
            c = College.objects.get(**kwargs)
            form1.college=c
            student.save()
            return redirect('allcolleges')
        return render(request, "addstudent.html", {'form1':form1,'form2':form2})