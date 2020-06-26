from django.shortcuts import render
from .models import Project

def index(requests):
    all_projects = Project.objects.all()
    return render(requests, 'portfolio/index.html', {'projects':all_projects})
