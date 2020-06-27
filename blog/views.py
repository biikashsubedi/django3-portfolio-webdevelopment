from django.shortcuts import render
from .models import Blog

def all_blog(request):
    all_blogs = Blog.objects.all()
    return render(request, 'blog/index.html', {'blogs': all_blogs})
