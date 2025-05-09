from django.shortcuts import render
from django.http.response import JsonResponse
# Create your views here




def first_task(request):
    guest=[
        {'id':1,
         'name':"kinana",
         "age":7876786,
         "studing":"eng"},
         {'id':2,
         'name':"kinana",
         "age":7876786,
         "studing":"eng"},
         {'id':3,
         'name':"kinana",
         "age":7876786,
         "studing":"eng"},
         {'id':4,
         'name':"kinana",
         "age":7876786,
         "studing":"eng"},
         {'id':5,
         'name':"kinana",
         "age":7876786,
         "studing":"eng"},
    ]
    return JsonResponse(guest,safe=False)