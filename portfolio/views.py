from django.shortcuts import HttpResponse
from django.shortcuts import render
from .models import Project 

# Create your views here.
def home(request):
    projects = Project.objects.all()  # get all object 'project' from DB
    return render(request, 'portfolio/home.html', {'projects':projects})
