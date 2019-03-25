from django.conf.urls import url

from django.views.generic import ListView, DetailView

from news.models import Articles

queryset = Articles.objects.all().order_by('-date')[:20]
urlpatterns = [
    url(r'^$', ListView.as_view(queryset=queryset, template_name='news/posts.html')),
    url(r'^/(?P<pk>\d+)$', DetailView.as_view(model=Articles, template_name='news/post.html'))


]
