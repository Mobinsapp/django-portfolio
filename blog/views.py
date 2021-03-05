from django.shortcuts import render, get_object_or_404
from django.shortcuts import HttpResponse
from .models import Blog 

# Create your views here.
# def home(request):
#     projects = Project.objects.all()  # get all object 'project' from DB
#     return render(request, 'portfolio/home.html', {'projects':projects})

def all_blogs(request):
    # blogs = Blog.objects.all()
    # blogs = Blog.objects.order_by('-date') : du plus recent au plus vieux
    blogs = Blog.objects.order_by('-date')[:3] #que les 5 derniers
    return render(request, 'blog/all_blogs.html', {'blogs' : blogs})

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog':blog})
