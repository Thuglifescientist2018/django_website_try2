from django.shortcuts import render
from .forms import BlogPostModelForm
from .models import BlogPost
from django.http import HttpResponse
# Create your views here.


def list_blogs(request):
    template_name = "blog_list.html"
    blogs = BlogPost.objects.all()
    context = {"blogs": blogs}
    return render(request, template_name, context)


def create_blog(request):
    template_name = "create_blog.html"
    form = BlogPostModelForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = BlogPostModelForm()
    context = {"form": form}
    return render(request, template_name, context)


def read_blog(request, slug):
    template_name = "readblog.html"
    blog_obj = BlogPost.objects.filter(slug=slug)
    if blog_obj.count() >= 1:
        blog_obj = blog_obj.first()
    context = {"blog": blog_obj}
    return render(request, template_name, context)


def update_blog(request, slug):
    template_name = "update_blog.html"
    blog_obj = BlogPost.objects.get(slug=slug)
    form = BlogPostModelForm(request.POST or None, instance=blog_obj)
    if form.is_valid():
        form.save()
    context = {"blog": blog_obj, "form": form}
    return render(request, template_name, context)
