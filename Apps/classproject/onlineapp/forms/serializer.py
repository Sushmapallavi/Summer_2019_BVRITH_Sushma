from django.conf.urls import url, include
from django.contrib.auth.models import User
from onlineapp.models import *
from rest_framework import routers, serializers, viewsets


class CollegeSerializer(serializers.ModelSerializer):
    class Meta:
        model = College
        fields = ('name', 'location', 'acronym', 'location')

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id','name','dob','email','db_folder','dropped_out')


class MocktestSerializer(serializers.ModelSerializer):
    class Meta:
        model = MockTest1
        fields = ('id', 'problem1','problem2','problem3','problem4','total')