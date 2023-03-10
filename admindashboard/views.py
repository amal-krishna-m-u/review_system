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



    from django.shortcuts import render, redirect
from .models import User
from .forms import AddUserForm

def add_user(request):
    if request.method == 'POST':
        form = AddUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            is_admin = form.cleaned_data['is_admin']
            user = User.objects.create_user(username=username, password=password)
            user.is_admin = is_admin
            user.save()
            return redirect('index')
    else:
        form = AddUserForm()
    return render(request, 'add_user.html', {'form': form})

def remove_user(request, username):
    user = User.objects.get(username=username)
    user.delete()
    return redirect('index')

