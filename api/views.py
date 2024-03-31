from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse

# Create your views here.

# def studentDetails(request):
#     student_details=Student.objects.get(id=1)# this method is used when we want to get the data of a particular id
#     # print(student_details)
#     serializer=StudentSerializer(student_details)
#     # print(serializer.data)
#     json_data=JSONRenderer().render(serializer.data)
#     # print(json_data)
#     return HttpResponse(json_data,content_type='application/json')


#to work with queryset or to show all the data of the student 
def studentDetails_queryset(request):
    student_details=Student.objects.all()
    # print(student_details)
    serializer=StudentSerializer(student_details, many=True)
    # print(serializer.data)
   
    # print(json_data)
    return JsonResponse(serializer.data,safe=False)#if safe=false is not given then it will raise an exception because non-dict objects can not be serialized and returned with jsonresponse funct


