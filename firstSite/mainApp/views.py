from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def mainApp(request):
    return HttpResponse('<center><h2>Hello World this is my first Web 2 Page!!!</h2</center>')

