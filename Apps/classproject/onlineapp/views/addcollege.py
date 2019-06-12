from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import *
from django.views import View
from onlineapp.forms.addcollege import CollegeForm
from onlineapp.models import *
from django.urls import resolve


class AddcollegeView(LoginRequiredMixin,View):
    login_url='/login/'
    def get(self,request,*args,**kwargs):
        form = CollegeForm()
        if resolve(request.path_info).url_name=='deletecolleges':
            college = College.objects.get(id = kwargs['id']).delete()
            return redirect("allcolleges")
        if kwargs:
            college=College.objects.get(**kwargs)
            form = CollegeForm(instance=college)

        return render(request,"addcollege.html",{'form':form})

    def post(self,request,*args,**kwargs):

        if resolve(request.path_info).url_name=='editcolleges':
            college = College.objects.get(id = kwargs['id'])
            form = CollegeForm(request.POST,instance=college)
            if form.is_valid:
                form.save()
                return redirect("allcolleges")


        form = CollegeForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect("allcolleges")
        return render(request, "addcollege.html", {'form': form})




