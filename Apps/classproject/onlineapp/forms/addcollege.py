from django import forms
from onlineapp.models import *

class CollegeForm(forms.ModelForm):
    class Meta:
        model = College
        exclude = ['id']
        fields = ('name','location','acronym','contact')
       # widgets = {
         #   'name': forms.charField(attrs={'class':'input', 'placeholder':"enter name"}),
        #    'location': forms.charField(attrs={'class': 'input', 'placeholder': "enter name"}),
          #  'email': forms.emailField(attrs={'class': 'input', 'placeholder': "enter name"}),
           # 'contact': forms.charField(attrs={'class': 'input', 'placeholder': "enter name"})
        #}


