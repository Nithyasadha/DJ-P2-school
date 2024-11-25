from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse 

def english(request):
    return HttpResponse('<h1>Most common language for everyone</h1>')
