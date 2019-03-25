from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def post_list(request):
    names = ['Oleg', 'Masha', 'Olya', 'Ksyusha']

    return render(request, 'blog/index.html', context={'names': names})
