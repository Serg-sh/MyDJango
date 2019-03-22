from django.urls import path
from django.views.generic import ListView

from news.models import Articles

queryset = Articles.objects.all().order_by('-date')[20]
template_name = 'news/posts.html'
urlpatterns = [
    path('', ListView.as_view(queryset=queryset, template_name=template_name)),
]
