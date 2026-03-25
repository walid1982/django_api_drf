from django.http import HttpResponse
from django.shortcuts import render
def bloogers(request):
    blooger =[
        {
        'id': 1,
        'name': 'Jane Doeffffffff',
        'designation': 'Software Engineersssssssssssss'
        }
        ]
    return HttpResponse(blooger)