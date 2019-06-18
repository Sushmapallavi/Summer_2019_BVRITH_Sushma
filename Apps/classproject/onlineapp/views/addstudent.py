from django.views import View
from onlineapp.forms.addstudent import StudentForm
from onlineapp.forms.mocktest import MarksForm
from onlineapp.models import *
from django.shortcuts import render
from django.shortcuts import *
from django.urls import resolve
from onlineapp.views import College


class AddstudentView(View):
    def get(self,request,**kwargs):
        if resolve(request.path_info).url_name == 'deletestudent':
            MockTest1.objects.get(student_id=kwargs.get('id')).delete()
            Student.objects.get(id=kwargs.get('id')).delete()
            return redirect('allcolleges')
        form1 = StudentForm()
        form2 = MarksForm()
        return render(request,"addstudent.html",{'form1':form1,'form2':form2})

    def post(self,request,*args,**kwargs):
        if resolve(request.path_info).url_name == 'edit_student':
            student = Student.objects.get(id=kwargs.get('id'))
            marks = MockTest1.objects.get(student_id=kwargs.get('id'))
            form1 = StudentForm(request.POST, instance=student)
            form2 = MarksForm(request.POST, instance=marks)
            if form1.is_valid() and form2.is_valid():
                form1.save()
                marks = form2.save(commit=False)
                marks.total = marks.problem1 + marks.problem2 + marks.problem3 + marks.problem4
                marks.save()
            return redirect('colleges_html')
        form1 = StudentForm(request.POST)
        form2 = MarksForm(request.POST)
        if form1.is_valid() and form2.is_valid():
            c = College.objects.get(**kwargs)
            student = form1.save(commit=False)
            student.college = c
                #College.objects.get(pk=kwargs.get('pk'))
            student.save()
            marks = form2.save(commit=False)
            marks.student_id = student.id
            marks.total = marks.problem1 + marks.problem2 + marks.problem3 + marks.problem4
            marks.save()
            return redirect('allcolleges')
        return render(request, "addstudent.html", {'form1':form1,'form2':form2})