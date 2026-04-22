from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.models import User
from .forms import RegisterForm

# Create your views here.
def register(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('user_dashboard:home')
    return render(request, 'users/registerForm.html', {'form':form})

def userlogout(request):
    logout(request)
    return redirect('users:login')