from django.shortcuts import render
from .models import Project 
from django.shortcuts import render, get_object_or_404


def home(request):
    # Grab all projects from the database
    projects = Project.objects.all() 
    
    # Pass them into the 'context' dictionary
    context = {'projects': projects}
    return render(request, 'home.html', context)


def machine_detail(request, pk):
    # This finds the machine by its ID (pk) or shows a 404 error
    machine = get_object_or_404(Project, pk=pk)
    return render(request, 'machine_detail.html', {'machine': machine})

def all_products(request):
    # Change 'Product' to 'Project'
    products = Project.objects.all() 
    context = {'projects': products}
    return render(request, 'home.html', context) # or your listing page