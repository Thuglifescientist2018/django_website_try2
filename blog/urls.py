from website.views import home
from django.urls import path
from .views import list_blogs, create_blog, read_blog, update_blog

urlpatterns = [
    path('', list_blogs, name="blog_list"),

    path('create', create_blog),
    path('edit/<str:slug>', update_blog),
    path('read/<str:slug>', read_blog, name="read_blog"),
]
