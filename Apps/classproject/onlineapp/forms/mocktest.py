from django import forms
from onlineapp.models import *

class MarksForm(forms.ModelForm):
    class Meta:
        model = MockTest1
        exclude = ['id','total','student_id']
        fields = ('problem1','problem2','problem3','problem4')