from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def thenmozhi(request):
    return HttpResponse('<h1> she is my class advisor</h1>' )
