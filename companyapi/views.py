from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
def home_page(request):
    print("This is home page Response")
    friends=[
        'arun',
        'rahul',
        'ram'
    ]
    return JsonResponse(friends,safe=False)