from onlineapp.forms.serializer import CollegeSerializer
from onlineapp.models import College
from rest_framework import permissions, status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


@api_view(['GET','POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def Collegeserializer(request):
    if request.method == 'GET':
        colleges = College.objects.all()
        collegeserializerdata = CollegeSerializer(colleges,many=True)
        return Response(collegeserializerdata.data,status=status.HTTP_200_OK)

    if request.method == 'POST':
        # college = request.data.get('College')
        serializer = CollegeSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data,status=status.HTTP_200_OK)


@api_view(['GET', 'PUT', 'DELETE'])
def colleges_detail(request, pk):
    try:
        college = College.objects.get(pk=pk)
    except College.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CollegeSerializer(college)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CollegeSerializer(college, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        college.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


