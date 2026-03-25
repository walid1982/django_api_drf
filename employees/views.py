from django.http import HttpResponse
from django.shortcuts import render
def employees(request):
    employee =[
        {
        'id': 1,
        'name': 'Jane Doeffffffff',
        'designation': 'Software Engineer'
        }
        ]
    return HttpResponse(employee)