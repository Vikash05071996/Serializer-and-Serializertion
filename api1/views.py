
from .models import Student
from .serializers import StudentSerializers
from rest_framework.renderers import JSONRenderer
from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def Student_detail(request,v):
    stu = Student.objects.get(id=v)
    serializer =StudentSerializers(stu)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data)
def Student_list(request):
    stu = Student.objects.all()
    serializer =StudentSerializers(stu,many=True)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data)

