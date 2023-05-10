
from .models import Student
from .serializers import StudentSerializers
from rest_framework.renderers import JSONRenderer
from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def Student_detail(request,v):
    stu = Student.objects.get(id=v)
    print(stu,"reading stu")
    serializer =StudentSerializers(stu)
    print(serializer)
    json_data = JSONRenderer().render(serializer.data)
    print(json_data)
    return HttpResponse(json_data)
def Student_list(request):
    stu = Student.objects.all()
    print(stu,"reading stu")
    serializer =StudentSerializers(stu,many=True)
    print(serializer)
    json_data = JSONRenderer().render(serializer.data)
    print(json_data)
    return HttpResponse(json_data)

