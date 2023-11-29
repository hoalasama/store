from django.shortcuts import render
from .models import Stuff
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from django.views import View
from .forms import StuffForm
from django.shortcuts import render, get_object_or_404  
from django.http import HttpResponse
# Create your views here.

def index(request):
    stuff = Stuff.objects.all().order_by('name')
    categories = Stuff.objects.values_list('category', flat=True).distinct()

    return render(request, 'homepage/index.html', {'stuff': stuff, 'categories': categories})

def get_category_items(request, category):
    items = Stuff.objects.filter(category=category)
    categories = Stuff.objects.values_list('category', flat=True).distinct()
    return render(request, 'homepage/category_items.html', {'items': items, 'selected_category': category, 'categories': categories})

def custom_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None and user.is_superuser:
                login(request, user)
                messages.success(request, f'Welcome, {username}!')
                return redirect('homepage')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()

    return render(request, 'login/login.html', {'form': form})

class LogoutView(View):
    def post(self, request):
        auth.logout(request)
        return redirect('homepage')
    
def add_stuff(request):
    if request.method == 'POST':
        form = StuffForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = StuffForm()

    return render(request, 'homepage/adding.html', {'form': form})

def stuff_detail(request, pk):
    stuff_item = get_object_or_404(Stuff, pk=pk)
    return render(request, 'homepage/detail.html', {'stuff_item': stuff_item})

def delete_stuff(request, pk):
    stuff=Stuff.objects.get(pk=pk)
    stuff.delete()
    return redirect('homepage')

def stuff_edit(request, pk):
    stuff_item = get_object_or_404(Stuff, pk=pk)
    if request.method == 'POST':
        form = StuffForm(request.POST, request.FILES, instance=stuff_item)
        if form.is_valid():
            form.save()
            return redirect('stuff_detail', pk=pk)
    else:
        form = StuffForm(instance=stuff_item)

    return render(request, 'homepage/stuff_edit.html', {'form': form, 'stuff_item': stuff_item})