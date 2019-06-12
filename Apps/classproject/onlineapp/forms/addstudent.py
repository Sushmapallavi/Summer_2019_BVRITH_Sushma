from django import forms
from onlineapp.models import *

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        exclude = ['dob','id','college_id']
        fields = ('name','email','db_folder','dropped_out')
