from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from onlineapp.models import *
from django.shortcuts import render
import logging

class CollegeView(LoginRequiredMixin,View):
    login_url='/login/'
    def get(self, request,*args,** kwargs):
        logging.error("college error log")
        logging.info("college info log")
        if(kwargs):
            s = Student.objects.values('name','college__name','college__id','college__acronym','mocktest1__total','id').filter(college__acronym=kwargs['acronym'])
            return render(
                request,
                template_name="marks.html",
                context={
                    'cid': kwargs['acronym'],
                    'jails': s,
                    'title': 'all students'
                }
            )
        colleges = College.objects.all()
        return render(
            request,
            template_name="colleges.html",
            context={
                'jails':colleges,
                'title' : 'all colleges'
            }
        )

