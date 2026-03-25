from django.http import HttpResponse
from django.shortcuts import render

def students(request):
    student =[
        {
        'id': 1,
        'name': 'John Doe',
        'age': 20
        }
        ]
    return HttpResponse(student)
