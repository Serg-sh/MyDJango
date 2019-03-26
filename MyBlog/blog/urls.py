"""MyBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from .views import *

urlpatterns = [

    path('', post_list, name='posts_list_url'),
    path('post/<str:slug>/', PostDetail.as_view(), name='posts_detail_url'),
    path('tags/', tags_list, name='tags_list_url'),
    path('tag/<str:slug>/', TagDetail.as_view(), name='tag_detail_url'),
]
