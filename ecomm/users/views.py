from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import RegisterForm

# Create your views here.
def register(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('dashboard:home')
    return render(request, 'users/registerForm.html', {'form':form})