from django.conf.urls import include,url
from django.views.generic import ListView,DetailView
from django.conf import settings
from django.conf.urls.static import static
from blog.models import Post
from blog import views
urlpatterns=[
    url(r'^$',ListView.as_view(
        queryset=Post.objects.all().order_by("-date")[:5],
        template_name="blog.html")),
    url(r'^(?P<pk>\d+)$',DetailView.as_view(
        model=Post,
        template_name="post.html")),
    url(r'^archives/$',ListView.as_view(
        queryset=Post.objects.all().order_by("-date"),
        template_name="archives.html")),
    url(r'^latestnews/$',ListView.as_view(
        queryset=Post.objects.all().order_by("-date")[:5],
        template_name="latestnews.html")),
    url(r'^sample_graph/$',views.graph, name='graph'),
]
