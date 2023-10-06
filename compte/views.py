from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.
# @login_required
def index(request):
    user = request.user
    return render(request, 'compte/index.html', {'user': user})


def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:     
                login(request, user)              
                return redirect('index')               
            else:
                messages.error(request, "Vous etez pas encore client")
                return render(request, 'compte/login.html', {})
        else:
            return render(request, 'compte/login.html', {})
    else:
        return redirect('index')


def logout_view(request):
    logout(request)
    return redirect('login')