from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Category

def index(request):
    categories = Category.objects.all()
    return render(request, 'admindashboard/index.html', {'categories': categories})

def add_category(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        Category.objects.create(name=name)
    return render(request, 'admindashboard/add_category.html')

def edit_category(request, pk):
    category = Category.objects.get(pk=pk)
    if request.method == 'POST':
        name = request.POST.get('name')
        category.name = name
        category.save()
    return render(request, 'admindashboard/edit_category.html', {'category': category})

def delete_category(request, pk):
    category = Category.objects.get(pk=pk)
    category.delete()
    return render(request, 'admindashboard/delete_category.html')
