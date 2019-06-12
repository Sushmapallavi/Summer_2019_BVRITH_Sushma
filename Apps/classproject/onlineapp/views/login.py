from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View
from onlineapp.forms.login import *
from django.contrib import messages

def logout_user(request):
    logout(request)
    return redirect('login')

class LoginView(View):
    def get(self,request):
        form = LoginForm()
        return render(request, "login.html", {'form': form})

    def post(self,request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect("allcolleges")
            else:
                messages.error(request, 'username or password not correct')
                return redirect('login')
        else:
            return redirect('login')



class SignupView(View):
    def get(self,request):
        form = SignupForm()
        return render(request, "signup.html", {'form': form})

    def post(self,request):
        form = SignupForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(**form.cleaned_data)
            #username = form.cleaned_data['username']
            #password = form.cleaned_data['password']
            user.save()
            if user is not None:
                login(request,user)
                return redirect('allcolleges')
            else:
                messages.error(request, 'invalid credentials')
                return redirect('signup')
        return render(request, "signup.html", {'form': form})


