from django.shortcuts import render, get_object_or_404

from .models import Blog
# Create your views here.
theblogs = Blog.objects
def allblogs(request):
    return render(request, 'blog/allblogs.html', {'theblogs': theblogs})

def detail(request, blog_id):
    detailblog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog':detailblog})