from django.http import HttpResponse
from django.shortcuts import render
def blogs(request):
    blog =[
        {
        'id': 1,
        'name': 'Jane Doe',
        'designation': 'Software Engineer'
        }
        ]
    return HttpResponse(blog)