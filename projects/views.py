from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def login_view(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return render(request, 'login.html')
    else:
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username = username, password = password)
        if user != None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Usuario o contraseña incorrectos'})

def logout_view(request):
    logout(request)
    return redirect('index')

def register_view(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('home')
        else:
            form = UserCreationForm()
            return render(request, 'register.html', {'register_form': form})
    else:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'register.html', {'register_form': form})
        
def home_view(request):
    return render(request, 'home.html')

def index_view(request):
    return render(request, 'index.html')