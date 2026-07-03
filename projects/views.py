from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
# Create your views here.
def login_view(request):
    if request.method == 'GET':
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

def home_view(request):
    return render(request, 'home.html')

def index_view(request):
    return render(request, 'index.html')