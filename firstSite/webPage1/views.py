from django.http import HttpResponse


# Create your views here.

def index(request):
    return HttpResponse('<center><h2>Hello World this is my first Web Page!!!</h2</center>')
