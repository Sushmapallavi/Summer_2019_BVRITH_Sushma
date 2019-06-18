from onlineapp.forms.serializer import StudentSerializer, MocktestSerializer
from onlineapp.models import *
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class Studentserializer(APIView):
    def get(self, request, **kwargs):
        students = Student.objects.all().filter(college_id=kwargs['pk'])
        serializer = StudentSerializer(students,many=True)
        return Response(serializer.data)

    def post(self, request, **kwargs):
        c = College.objects.get(**kwargs)
        s = Student(college=c)
        studserializer = StudentSerializer(s,data=request.data)
        mockserializer = MocktestSerializer(data=request.data['test'])
        if studserializer.is_valid() and mockserializer.is_valid():
            studserializer.save(college=c)
            mockserializer.save(stduent=s)
            return Response(studserializer.data,status=status.HTTP_200_OK)


class StudentDetail(APIView):
    def get_object(self, pk,cid):
        try:
            students = Student.objects.all().filter(college_id=pk)
            return MockTest1.objects.all().filter(student_id=cid)
        except MockTest1.DoesNotExist:
            raise Http404

    def get(self, request, pk, cid):
        marks = self.get_object(pk,cid)
        serializer = MocktestSerializer(marks, many=True)
        return Response(serializer.data)

    def delete(self, request, pk, cid):
        marks = self.get_object(pk,cid)
        marks.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



